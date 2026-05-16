from django.db import models
from django.conf import settings    # Pour récupérer AUTH_USER_MODEL proprement
from restaurant.models import Table
from menu.models import Plat

# Représente une commande passée par un client
class Commande(models.Model):
    
    # Les états possibles d'une commande
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),   # Commande créée, pas encore traitée
        ('en_preparation', 'En préparation'), # En préparation en cuisine
        ('pret_a_servir', 'Prêt à servir'), # Prête pour le serveur
        ('servie', 'Servie'),           # Apportée à la table
        ('terminee', 'Terminée'),       # Commande terminée
        ('payee', 'Payée'),             # Client a payé, commande terminée
    ]
    
    PRIORITE_CHOICES = [
        ('normal', 'Normal'),
        ('urgent', 'Urgent'),
    ]
    
    # La table concernée par cette commande
    # CASCADE = si on supprime la table, la commande est supprimée aussi
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE
    )
    
    # Le client qui a passé la commande (optionnel)
    # SET_NULL = si on supprime le client, la commande reste mais sans client
    # On utilise settings.AUTH_USER_MODEL au lieu d'importer directement
    # pour éviter les problèmes de circular import
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,      # Peut être vide en base de données
        blank=True      # Peut être vide dans les formulaires
    )
    
    # Les plats commandés (plusieurs plats par commande possible)
    # ManyToMany = une commande peut avoir plusieurs plats
    #              un plat peut être dans plusieurs commandes
    plats = models.ManyToManyField(Plat)
    
    # État actuel de la commande
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente'
    )
    
    # Priorité de la commande
    priorite = models.CharField(
        max_length=20,
        choices=PRIORITE_CHOICES,
        default='normal'
    )
    
    # Préférences du client (likes)
    preferences = models.TextField(blank=True, null=True)
    
    # Aversions du client (dislikes)
    aversions = models.TextField(blank=True, null=True)
    
    # Allergies du client (très important)
    allergies = models.TextField(blank=True, null=True)
    
    # Notes pour le serveur/admin
    notes = models.TextField(blank=True, null=True)
    
    # Date et heure de création, remplie automatiquement
    date_creation = models.DateTimeField(auto_now_add=True)
    
    # Date et heure de début de préparation
    date_debut_preparation = models.DateTimeField(blank=True, null=True)
    
    # Date et heure de fin de préparation
    date_fin_preparation = models.DateTimeField(blank=True, null=True)
    
    # Total calculé de la commande (mis à jour via la logique métier)
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    # Calcul automatique du total de la commande
    def calculate_total(self):
        total = sum(plat.prix for plat in self.plats.all())
        self.total = total
        self.save()

    def __str__(self):
        return f"Commande #{self.id} - Table {self.table.numero}"