from django.urls import path
from . import views

urlpatterns = [

    # Route pour afficher toutes les tables
    path(
        'tables/',
        views.liste_tables,
        name='liste_tables'
    ),

    # Route pour modifier l'état d'une table
    path(
        'tables/modifier/<int:table_id>/',
        views.modifier_table,
        name='tables_list'
    ),
]