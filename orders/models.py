from django.db import models

# Modèle représentant une commande dans le restaurant
class Commande(models.Model):
    # Utilisateur qui passe la commande
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    
    # Table concernée par la commande
    table = models.ForeignKey('restaurant.Table', on_delete=models.CASCADE)
    
    # Plat commandé
    plat = models.ForeignKey('menu.Plat', on_delete=models.CASCADE)

    # Quantité commandée
    quantity = models.IntegerField(default=1)

    # Date de création automatique de la commande
    created_at = models.DateTimeField(auto_now_add=True)

    # Affichage de la commande dans l'admin
    def __str__(self):
        return f"Commande {self.id} - {self.user.name}"