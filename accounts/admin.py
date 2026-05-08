from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# On utilise UserAdmin pour avoir tous les champs
# de gestion des utilisateurs (password, permissions...)
@admin.register(User)                    # ← le @ est important !
class CustomUserAdmin(UserAdmin):
    # Colonnes affichées dans la liste des utilisateurs
    list_display = ('username', 'email', 'role', 'is_staff')
    # Filtre par rôle sur la droite
    list_filter = ('role',)
    # Ajouter le champ rôle dans le formulaire d'édition
    fieldsets = UserAdmin.fieldsets + (
        ('Rôle', {'fields': ('role',)}),
    )