from django.urls import path
from . import views

urlpatterns = [
    # Route pour afficher toutes les commandes
    path('commandes/', views.commandes_list, name='commandes_list'),
    # Route pour créer une commande
    path('commandes/creer/', views.create_commande, name='create_commande'),
]