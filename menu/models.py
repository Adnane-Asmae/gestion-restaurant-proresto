from django.db import models

# Create your models here.
from django.db import models

# Modèle représentant un plat
class Plat(models.Model):
    # Nom du plat
    name = models.CharField(max_length=100)

    # Prix du plat
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # Description optionnelle
    description = models.TextField(blank=True)

    # Affichage dans l'admin
    def __str__(self):
        return self.name