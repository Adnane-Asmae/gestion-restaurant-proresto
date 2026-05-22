
from django.urls import path
from .views import chatbot_view, chatbot_response_view

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot_view'),
    path('chatbot/response/', chatbot_response_view, name='chatbot_response'),
]

