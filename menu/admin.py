from django.contrib import admin
from .models import Plat

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('nom', 'prix', 'disponible')
    # Filtre par disponibilité
    list_filter = ('disponible',)
    # Barre de recherche par nom
    search_fields = ('nom',)