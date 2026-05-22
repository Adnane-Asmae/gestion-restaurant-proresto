
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('me/', views.get_current_user, name='current_user'),
    
    # Users endpoints
    path('users/', views.users_list, name='users-list'),
    path('users/<int:pk>/', views.users_detail, name='users-detail'),
    path('users/create/', views.users_create, name='users-create'),
    path('users/<int:pk>/update/', views.users_update, name='users-update'),
    path('users/<int:pk>/delete/', views.users_delete, name='users-delete'),
]

