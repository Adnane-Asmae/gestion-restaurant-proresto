from django.contrib.auth.models import AbstractUser
from django.db import models

# On hérite de AbstractUser pour garder toutes les fonctionnalités
# de base de Django (login, password, etc.) et on ajoute juste le rôle
class User(AbstractUser):
    
    # Les choix possibles pour le rôle de l'utilisateur
    ROLE_CHOICES = [
        ('admin', 'Admin'),       # Gérant du restaurant
        ('serveur', 'Serveur'),   # Prend les commandes
        ('client', 'Client'),     # Passe les commandes
    ]
    
    # Champ rôle : obligatoire, par défaut = client
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='client'
    )

    # Ce qu'on affiche quand on voit un utilisateur dans l'admin
    def __str__(self):
        return f"{self.username} ({self.role})"