import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Plat
from restaurant.models import Table

# Créer des plats
plats_data = [
    {"nom": "Tajine Poulet", "description": "Tajine de poulet aux olives et citrons confits", "prix": 65.00},
    {"nom": "Couscous Royal", "description": "Couscous aux légumes et viande", "prix": 75.00},
    {"nom": "Pastilla", "description": "Pastilla sucrée-salée aux amandes", "prix": 55.00},
    {"nom": "Harira", "description": "Soupe traditionnelle marocaine", "prix": 25.00},
    {"nom": "Baklava", "description": "Dessert aux noix et miel", "prix": 30.00},
]

for data in plats_data:
    Plat.objects.get_or_create(**data)

# Créer des tables
tables_data = [
    {"numero": 1, "capacite": 2, "est_occupee": False},
    {"numero": 2, "capacite": 4, "est_occupee": False},
    {"numero": 3, "capacite": 4, "est_occupee": True},
    {"numero": 4, "capacite": 6, "est_occupee": False},
    {"numero": 5, "capacite": 2, "est_occupee": False},
]

for data in tables_data:
    Table.objects.get_or_create(**data)

print("Sample data created successfully!")
