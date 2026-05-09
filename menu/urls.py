from django.urls import path
from . import views

urlpatterns = [
    # Route pour afficher tous les plats
    path('plats/', views.liste_plats, name='liste_plats'),
]