from django.db import models

# Modèle représentant un utilisateur
class User(models.Model):

    # Les rôles possibles de l'utilisateur
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('serveur', 'Serveur'),
        ('client', 'Client'),
    ]

    # Nom de l'utilisateur
    name = models.CharField(max_length=100)

    # Rôle de l'utilisateur (choix limité)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    # Affichage du nom dans l'admin
    def __str__(self):
        return self.name
    


        # Modèle représentant une table du restaurant
class Table(models.Model):
    number = models.IntegerField()       # Numéro de la table
    is_occupied = models.BooleanField(default=False)  # Est-elle occupée ?

    def __str__(self):
        return f"Table {self.number}"
    

    # Modèle représentant un plat du restaurant
class Plat(models.Model):
    name = models.CharField(max_length=100)       # Nom du plat
    price = models.DecimalField(max_digits=6, decimal_places=2)  # Prix du plat
    description = models.TextField(blank=True)    # Description (optionnelle)

    def __str__(self):
        return self.name  # Affiche le nom dans l'admin
    
    
    
    # Modèle représentant une commande
class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)       # L'utilisateur qui passe la commande
    table = models.ForeignKey(Table, on_delete=models.CASCADE)     # La table concernée
    plat = models.ForeignKey(Plat, on_delete=models.CASCADE)       # Le plat commandé
    quantity = models.IntegerField(default=1)                       # Quantité commandée
    created_at = models.DateTimeField(auto_now_add=True)            # Date et heure de la commande

    def __str__(self):
        return f"Commande {self.id} - {self.user.name}"  # Affiche l'ID et le nom de l'utilisateur