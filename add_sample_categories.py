
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Categorie, Plat

# Sample categories
categories_data = [
    {'nom': 'Entrées', 'ordre': 1},
    {'nom': 'Plats principaux', 'ordre': 2},
    {'nom': 'Desserts', 'ordre': 3},
    {'nom': 'Boissons', 'ordre': 4},
]

# Create categories
for cat_data in categories_data:
    cat, created = Categorie.objects.get_or_create(nom=cat_data['nom'], defaults=cat_data)
    if created:
        print(f"Created category: {cat.nom}")

# Assign categories to plats
plat_category_mapping = {
    'Harira': 'Entrées',
    'Gazpacho': 'Entrées',
    'Patatas Bravas': 'Entrées',
    'Tagine': 'Plats principaux',
    'Couscous': 'Plats principaux',
    'Pastilla': 'Plats principaux',
    'Paella': 'Plats principaux',
    'Tortilla Española': 'Plats principaux',
    'Pizza Margherita': 'Plats principaux',
    'Pasta Carbonara': 'Plats principaux',
    'Lasagna': 'Plats principaux',
    'Risotto': 'Plats principaux',
    'Peking Duck': 'Plats principaux',
    'Dim Sum': 'Plats principaux',
    'Kung Pao Chicken': 'Plats principaux',
    'Sweet and Sour Chicken': 'Plats principaux',
    'Chow Mein': 'Plats principaux',
    'Sushi': 'Plats principaux',
    'Ramen': 'Plats principaux',
    'Tempura': 'Plats principaux',
    'Yakitori': 'Plats principaux',
    'Tiramisu': 'Desserts',
    'Mochi': 'Desserts',
}

for plat_nom, cat_nom in plat_category_mapping.items():
    try:
        plat = Plat.objects.get(nom=plat_nom)
        cat = Categorie.objects.get(nom=cat_nom)
        plat.categorie = cat
        plat.save()
        print(f"Assigned {plat.nom} to {cat.nom}")
    except Plat.DoesNotExist:
        print(f"Plat not found: {plat_nom}")
    except Categorie.DoesNotExist:
        print(f"Categorie not found: {cat_nom}")

print("\nDone!")
