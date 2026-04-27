from django.db import models

# Create your models here.


# Modèle représentant un utilisateur
class User(models.Model):
    # Rôles possibles
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('serveur', 'Serveur'),
        ('client', 'Client'),
    ]

    # Nom de l'utilisateur
    name = models.CharField(max_length=100)

    # Rôle de l'utilisateur
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Affichage dans l'admin
    def __str__(self):
        return self.name