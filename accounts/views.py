
import json
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import User


logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    """Login user"""
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)
            return JsonResponse({
                'user': get_user_dict(user),
                'message': 'Login successful'
            })
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)
    except Exception as e:
        logger.error(f"Login error: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def logout_view(request):
    """Logout user"""
    logout(request)
    return JsonResponse({'message': 'Logout successful'})



def get_user_dict(user):
    """Convert User object to dictionary"""
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'role': user.role,
    }


@require_http_methods(["GET"])
@login_required
def get_current_user(request):
    """Get current authenticated user"""
    return JsonResponse(get_user_dict(request.user))


@require_http_methods(["GET"])
@login_required
def users_list(request):
    """Get all users (admin only)"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    try:
        users = User.objects.all()
        data = [get_user_dict(user) for user in users]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
@login_required
def users_detail(request, pk):
    """Get single user (admin only)"""
    if request.user.role != 'admin' and request.user.id != pk:
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    try:
        user = User.objects.get(pk=pk)
        return JsonResponse(get_user_dict(user))
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        logger.error(f"Error getting user {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
@login_required
def users_create(request):
    """Create new user (admin only)"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    try:
        data = json.loads(request.body)
        
        user = User.objects.create(
            username=data.get('username'),
            email=data.get('email', ''),
            role=data.get('role', 'server'),
        )
        
        if 'password' in data:
            user.set_password(data['password'])
            user.save()
            
        return JsonResponse(get_user_dict(user), status=201)
    except Exception as e:
        logger.error(f"Error creating user: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
@login_required
def users_update(request, pk):
    """Update user (admin or self)"""
    if request.user.role != 'admin' and request.user.id != pk:
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    try:
        user = User.objects.get(pk=pk)
        data = json.loads(request.body)
        
        if 'username' in data:
            user.username = data['username']
        if 'email' in data:
            user.email = data['email']
        if 'role' in data and request.user.role == 'admin':
            user.role = data['role']
            
        if 'password' in data:
            user.set_password(data['password'])
            
        user.save()
        return JsonResponse(get_user_dict(user))
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating user {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
@login_required
def users_delete(request, pk):
    """Delete user (admin only)"""
    if request.user.role != 'admin':
        return JsonResponse({'error': 'Not authorized'}, status=403)
        
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=204)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        logger.error(f"Error deleting user {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)

