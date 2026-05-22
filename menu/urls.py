
from django.urls import path
from . import views

urlpatterns = [
    # Categories endpoints
    path('categories/', views.categories_list, name='categories-list'),
    path('categories/<int:pk>/', views.categories_detail, name='categories-detail'),
    path('categories/create/', views.categories_create, name='categories-create'),
    path('categories/<int:pk>/update/', views.categories_update, name='categories-update'),
    path('categories/<int:pk>/delete/', views.categories_delete, name='categories-delete'),
    
    # Plats endpoints
    path('plats/', views.plats_list, name='plats-list'),
    path('plats/<int:pk>/', views.plats_detail, name='plats-detail'),
    path('plats/create/', views.plats_create, name='plats-create'),
    path('plats/<int:pk>/update/', views.plats_update, name='plats-update'),
    path('plats/<int:pk>/delete/', views.plats_delete, name='plats-delete'),
]

