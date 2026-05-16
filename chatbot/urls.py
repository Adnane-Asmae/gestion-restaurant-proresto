from django.urls import path
from .views import ChatbotView, ChatbotResponseView

urlpatterns = [
    path('chatbot/', ChatbotView.as_view(), name='chatbot_view'),
    path('chatbot/response/', ChatbotResponseView.as_view(), name='chatbot_response'),
]
