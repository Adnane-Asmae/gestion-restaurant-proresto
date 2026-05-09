from django.urls import path
from . import views

urlpatterns = [
    # Route pour afficher toutes les tables
    path('tables/', views.liste_tables, name='liste_tables'),
]