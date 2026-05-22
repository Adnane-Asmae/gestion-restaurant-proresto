
from django.urls import path
from . import views

urlpatterns = [
    # Commandes endpoints
    path('commandes/', views.commandes_list, name='commandes-list'),
    path('commandes/<int:pk>/', views.commandes_detail, name='commandes-detail'),
    path('commandes/create/', views.commandes_create, name='commandes-create'),
    path('commandes/<int:pk>/update/', views.commandes_update, name='commandes-update'),
    path('commandes/<int:pk>/delete/', views.commandes_delete, name='commandes-delete'),
]

