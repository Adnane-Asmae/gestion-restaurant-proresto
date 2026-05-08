from django.urls import path
from . import views

urlpatterns = [
    path('', views.commandes_list, name='commandes_list'),
    path('create/', views.create_commande, name='create_commande'),
]