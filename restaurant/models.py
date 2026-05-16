# Modèle représentant une table du restaurant
from django.db import models
from .utils import generate_qr_code


# Représente une table physique dans le restaurant
class Table(models.Model):
    
    # Numéro unique de la table (ex: Table 1, Table 2...)
    numero = models.IntegerField(unique=True)
    
    # Nombre de personnes que la table peut accueillir
    capacite = models.IntegerField()
    
    # État de la table : True = occupée, False = libre
    # Par défaut, toutes les tables sont libres
    est_occupee = models.BooleanField(default=False)
    
    # QR Code pour cette table
    qr_code = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generate QR code only if it doesn't exist
        if not self.qr_code:
            self.qr_code = generate_qr_code(self)
        super().save(*args, **kwargs)
    
    def regenerate_qr_code(self):
        # Force regenerate QR code
        if self.qr_code:
            self.qr_code.delete(save=False)
        self.qr_code = generate_qr_code(self)
        self.save()

    def __str__(self):
        return f"Table {self.numero}"


class CallServer(models.Model):
    STATUT_CHOICES = [
        ('pending', 'En attente'),
        ('resolved', 'Résolu'),
    ]
    
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='pending')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_resolution = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Appel serveur - Table {self.table.numero} ({self.statut})"