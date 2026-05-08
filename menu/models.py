from django.db import models

# Représente un plat dans le menu du restaurant
class Plat(models.Model):
    
    # Nom du plat (ex: "Tajine poulet", "Couscous")
    nom = models.CharField(max_length=100)
    
    # Description optionnelle du plat (ingrédients, allergènes...)
    description = models.TextField(blank=True)
    
    # Prix du plat avec 2 décimales (ex: 45.00 DH)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    
    # Si False, le plat n'apparaît pas dans le menu (rupture de stock)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nom