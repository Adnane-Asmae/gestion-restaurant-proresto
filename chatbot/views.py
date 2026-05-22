
import os
import json
import logging
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from menu.models import Plat
from restaurant.models import Table
from orders.models import Commande
from .models import ChatConversation, ChatMessage

# Configure logging
logger = logging.getLogger(__name__)

# Try to import OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logger.warning("OpenAI library not installed. Install with: pip install openai")


def get_system_prompt():
    """Generate the system prompt with restaurant context"""
    try:
        plats = Plat.objects.filter(disponible=True)
        menu_items = []
        for plat in plats:
            item = f"- {plat.nom}: {plat.prix} DH"
            if plat.description:
                item += f" - {plat.description}"
            menu_items.append(item)
        
        tables = Table.objects.all()
        table_info = []
        for table in tables:
            status = "Occupied" if table.est_occupee else "Available"
            table_info.append(f"- Table {table.numero}: {status}, Capacity: {table.capacite} people")
        
        system_prompt = f"""You are a friendly, professional restaurant waiter assistant for PRORESTO.

Your responsibilities:
1. Help customers with menu questions
2. Take food and drink orders
3. Answer questions about tables and availability
4. Make personalized recommendations
5. Handle special requests (allergies, modifications, etc.)

IMPORTANT: Keep your responses natural, conversational, and concise. Always be polite and helpful.

MENU (Available Dishes):
{chr(10).join(menu_items)}

TABLES:
{chr(10).join(table_info)}

Instructions:
- If the customer wants to order something, confirm the details (dish names, quantities, table number)
- If information is missing, ask clarifying questions
- If they ask for recommendations, suggest popular items from the menu
- Always stay in character as a professional restaurant waiter
- If you don't know something, politely offer to ask a human staff member
"""
        return system_prompt
    except Exception as e:
        logger.error(f"Error generating system prompt: {e}")
        return "You are a friendly restaurant waiter assistant for PRORESTO."


def get_or_create_conversation(request):
    """Get or create a conversation for the current session"""
    if not request.session.session_key:
        request.session.create()
    
    session_key = request.session.session_key
    conversation, created = ChatConversation.objects.get_or_create(
        session_key=session_key
    )
    
    # If new conversation, add system message
    if created:
        system_prompt = get_system_prompt()
        ChatMessage.objects.create(
            conversation=conversation,
            role='system',
            content=system_prompt
        )
    
    return conversation


def get_fallback_response(user_message):
    """Fallback response when OpenAI is not available"""
    user_message_lower = user_message.lower()
    
    # Simple keyword matching for fallback
    if any(keyword in user_message_lower for keyword in ['menu', 'what do you have', 'food', 'dishes']):
        try:
            plats = Plat.objects.filter(disponible=True)[:5]
            menu_text = "Here are some of our popular dishes:\n"
            for plat in plats:
                menu_text += f"• {plat.nom} - {plat.prix} DH\n"
            menu_text += "\nWould you like to order anything?"
            return menu_text
        except:
            return "I'd be happy to show you our menu! What kind of food are you in the mood for?"
    
    elif any(keyword in user_message_lower for keyword in ['order', 'want', 'i would like']):
        return "Great! What would you like to order? Please let me know the dish names and quantities."
    
    elif any(keyword in user_message_lower for keyword in ['table', 'tables', 'available']):
        try:
            tables = Table.objects.filter(est_occupee=False)
            if tables:
                table_text = "Here are our available tables:\n"
                for table in tables:
                    table_text += f"• Table {table.numero} - Capacity: {table.capacite} people\n"
                return table_text
            else:
                return "I'm sorry, all our tables are currently occupied."
        except:
            return "I can help you with table availability! Would you like me to check?"
    
    elif any(keyword in user_message_lower for keyword in ['hello', 'hi', 'hey']):
        return "Hello! Welcome to PRORESTO! How can I help you today? I can show you our menu, take your order, or help with table reservations."
    
    elif any(keyword in user_message_lower for keyword in ['thank', 'thanks']):
        return "You're very welcome! Enjoy your meal!"
    
    else:
        return "I'm here to help! I can assist with menu questions, orders, and table availability. What would you like to know?"


def call_openai_api(messages):
    """Call OpenAI API to generate response"""
    try:
        api_key = getattr(settings, 'OPENAI_API_KEY', None)
        
        if not api_key:
            logger.warning("OPENAI_API_KEY not set in settings")
            return get_fallback_response("")
        
        client = OpenAI(api_key=api_key)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        logger.error(f"OpenAI API error: {e}", exc_info=True)
        return get_fallback_response("")


def chatbot_view(request):
    return render(request, 'chatbot/chat.html')


@csrf_exempt
@require_http_methods(["POST"])
def chatbot_response_view(request):
    try:
        data = json.loads(request.body)
        user_message = data.get('message', '').strip()
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    
    logger.info(f"Received chat message: {user_message[:100]}")
    
    try:
        # Get or create conversation
        conversation = get_or_create_conversation(request)
        
        # Save user message
        ChatMessage.objects.create(
            conversation=conversation,
            role='user',
            content=user_message
        )
        
        # Get conversation history
        messages = conversation.messages.all()
        openai_messages = []
        for msg in messages:
            openai_messages.append({
                'role': msg.role,
                'content': msg.content
            })
        
        # Generate response
        if OPENAI_AVAILABLE:
            response_text = call_openai_api(openai_messages)
        else:
            response_text = get_fallback_response(user_message)
        
        # Save assistant response
        ChatMessage.objects.create(
            conversation=conversation,
            role='assistant',
            content=response_text
        )
        
        logger.info(f"Generated response: {response_text[:100]}")
        
        return JsonResponse({
            'response': response_text,
            'conversation_id': conversation.id
        })
        
    except Exception as e:
        logger.error(f"Error processing chat message: {e}", exc_info=True)
        return JsonResponse({
            'response': "I'm sorry, I'm having trouble right now. Please try again in a moment.",
            'conversation_id': None
        }, status=500)

