from django.contrib import admin
from .models import Commande

@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('id', 'table', 'client', 'statut', 'total', 'date_creation')
    # Filtre par statut
    list_filter = ('statut',)