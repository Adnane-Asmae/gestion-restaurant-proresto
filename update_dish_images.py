
import os
from pathlib import Path
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Plat

dish_image_map = {
    'Tagine': 'Tajine.jpg',
    'Couscous': 'Couscous.jpg',
    'Pastilla': 'Bastilla.jpg',
    'Bastilla': 'Bastilla.jpg',
    'Harira': 'Harira.jpg',
    'Moroccan Tea': 'Moroccan tea.jpg',
    'Sweets Prestige': 'Sweets Prestige.jpg',
    'Paella': 'Paella.jpg',
    'Tortilla': 'Tortilla.jpg',
    'Gazpacho': 'Gazpacho.jpg',
    'Patatas Bravas': 'Batatas bravas.jpg',
    'Churros': 'Churros with chocolate.jpg',
    'Pizza Margherita': 'Pizza margherita.jpg',
    'Pasta Carbonara': 'Pasta carbonara.jpg',
    'Lasagna': 'Lasagna.jpg',
    'Risotto': 'Risotto.jpg',
    'Tiramisu': None,  # uses Unsplash URL
    'Sushi Platter': None,  # uses Unsplash URL
    'Ramen Tonkotsu': None,  # uses Unsplash URL
    'Tempura': 'Tempura.jpg',
    'Yakitori': 'Yakitori.jpg',
    'Mochi': 'Mochi.jpg',
    'Peking Duck': 'Peking duck.jpg',
    'Kung Pao Chicken': 'Kung pao chicken.jpg',
    'Sweet and Sour Chicken': 'Sweet and sour chicken.jpg',
    'Dim Sum': 'Dim sum.jpg',
    'Chow Mein': 'Chow mein.jpg',
    'Rfissa': 'rfissa.jpg',
}

print("Updating dish images...")
for plat in Plat.objects.all():
    print(f"\nProcessing: {plat.nom}")
    if plat.nom in dish_image_map:
        image_file = dish_image_map[plat.nom]
        if image_file:
            plat.image_url = f'/media/plats/{image_file}'
            print(f"  Setting image_url to: {plat.image_url}")
        plat.save()
        print(f"  Saved!")
    else:
        print(f"  No image mapping found for this dish")

print("\nDone! All dishes updated!")
