from django.db import models

# Create your models here.
from django.db import models

# Modèle représentant une table du restaurant
class Table(models.Model):
    # Numéro de la table
    number = models.IntegerField()

    # Si la table est occupée ou non
    is_occupied = models.BooleanField(default=False)

    # Affichage dans l'admin
    def __str__(self):
        return f"Table {self.number}"