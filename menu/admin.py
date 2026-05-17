from django.contrib import admin
from .models import Categorie, Plat

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ordre')
    list_editable = ('ordre',)
    search_fields = ('nom',)

@admin.register(Plat)
class PlatAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'prix', 'disponible')
    list_filter = ('categorie', 'disponible')
    search_fields = ('nom',)