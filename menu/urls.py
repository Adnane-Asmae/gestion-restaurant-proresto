from django.urls import path
from . import views

urlpatterns = [
    # Route pour afficher tous les plats
    path('plats/', views.liste_plats, name='liste_plats'),
    # Route pour ajouter un plat
    path('plats/ajouter/', views.create_plat, name='create_plat'),
    # Route pour modifier un plat
    path('plats/modifier/<int:plat_id>/', views.update_plat, name='update_plat'),
    # Route pour supprimer un plat
    path('plats/supprimer/<int:plat_id>/', views.delete_plat, name='delete_plat'),
]