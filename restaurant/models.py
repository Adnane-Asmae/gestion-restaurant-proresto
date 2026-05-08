# Modèle représentant une table du restaurant
from django.db import models

# Représente une table physique dans le restaurant
class Table(models.Model):
    
    # Numéro unique de la table (ex: Table 1, Table 2...)
    numero = models.IntegerField(unique=True)
    
    # Nombre de personnes que la table peut accueillir
    capacite = models.IntegerField()
    
    # État de la table : True = occupée, False = libre
    # Par défaut, toutes les tables sont libres
    est_occupee = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.numero}"