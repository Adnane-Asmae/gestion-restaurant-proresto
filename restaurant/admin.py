from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('numero', 'capacite', 'est_occupee')
    # Filtre par état (occupée ou libre)
    list_filter = ('est_occupee',)