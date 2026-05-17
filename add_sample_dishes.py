
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Plat

# Sample dishes data
dishes_data = [
    # 🇲🇦 Morocco
    {
        'nom': 'Tagine',
        'pays': 'maroc',
        'description': 'Tender lamb with dried fruits and honey',
        'prix': 85.00,
        'disponible': True,
        'image_url': '/Tajine.jpg'
    },
    {
        'nom': 'Bastilla',
        'pays': 'maroc',
        'description': 'Savory-sweet pie with chicken and almonds',
        'prix': 65.00,
        'disponible': True,
        'image_url': '/Bastilla.jpg'
    },
    {
        'nom': 'Couscous',
        'pays': 'maroc',
        'description': 'Steamed semolina with vegetables and meat',
        'prix': 95.00,
        'disponible': True,
        'image_url': '/Couscous.jpg'
    },
    {
        'nom': 'Harira',
        'pays': 'maroc',
        'description': 'Traditional Moroccan soup with lentils and meat',
        'prix': 35.00,
        'disponible': True,
        'image_url': '/Harira.jpg'
    },
    {
        'nom': 'Sweets Prestige',
        'pays': 'maroc',
        'description': 'Traditional Moroccan sweets and pastries',
        'prix': 45.00,
        'disponible': True,
        'image_url': '/Sweets Prestige.jpg'
    },
    {
        'nom': 'Moroccan Tea',
        'pays': 'maroc',
        'description': 'Traditional Moroccan mint tea',
        'prix': 15.00,
        'disponible': True,
        'image_url': '/Moroccan tea.jpg'
    },
    
    # 🇪🇸 Spain
    {
        'nom': 'Paella',
        'pays': 'espagne',
        'description': 'Saffron rice with seafood and vegetables',
        'prix': 110.00,
        'disponible': True,
        'image_url': '/Paella.jpg'
    },
    {
        'nom': 'Gazpacho',
        'pays': 'espagne',
        'description': 'Cold tomato soup with fresh vegetables',
        'prix': 35.00,
        'disponible': True,
        'image_url': '/Gazpacho.jpg'
    },
    {
        'nom': 'Tortilla',
        'pays': 'espagne',
        'description': 'Traditional Spanish potato omelette',
        'prix': 55.00,
        'disponible': True,
        'image_url': '/Tortilla.jpg'
    },
    {
        'nom': 'Patatas Bravas',
        'pays': 'espagne',
        'description': 'Crispy potatoes with spicy tomato sauce',
        'prix': 45.00,
        'disponible': True,
        'image_url': '/Batatas bravas.jpg'
    },
    {
        'nom': 'Churros',
        'pays': 'espagne',
        'description': 'Fried dough with chocolate sauce',
        'prix': 40.00,
        'disponible': True,
        'image_url': '/Churros with chocolate.jpg'
    },
    
    # 🇮🇹 Italy
    {
        'nom': 'Pizza Margherita',
        'pays': 'italie',
        'description': 'Classic pizza with tomato, mozzarella, and basil',
        'prix': 80.00,
        'disponible': True,
        'image_url': '/Pizza margherita.jpg'
    },
    {
        'nom': 'Pasta Carbonara',
        'pays': 'italie',
        'description': 'Creamy pasta with pancetta and pecorino',
        'prix': 70.00,
        'disponible': True,
        'image_url': '/Pasta carbonara.jpg'
    },
    {
        'nom': 'Lasagna',
        'pays': 'italie',
        'description': 'Layered pasta with bolognese and bechamel sauce',
        'prix': 85.00,
        'disponible': True,
        'image_url': '/Lasagna.jpg'
    },
    {
        'nom': 'Risotto',
        'pays': 'italie',
        'description': 'Creamy rice with mushrooms and parmesan',
        'prix': 82.00,
        'disponible': True,
        'image_url': '/Risotto.jpg'
    },
    {
        'nom': 'Tiramisu',
        'pays': 'italie',
        'description': 'Coffee-soaked ladyfingers with mascarpone',
        'prix': 45.00,
        'disponible': True,
        'image_url': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?q=80&w=800&auto=format&fit=crop'
    },
    
    # 🇯🇵 Japan
    {
        'nom': 'Sushi Platter',
        'pays': 'japon',
        'description': 'Assorted fresh sushi and sashimi',
        'prix': 120.00,
        'disponible': True,
        'image_url': 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Ramen Tonkotsu',
        'pays': 'japon',
        'description': 'Rich pork bone broth with noodles',
        'prix': 85.00,
        'disponible': True,
        'image_url': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Tempura',
        'pays': 'japon',
        'description': 'Lightly battered shrimp and vegetables',
        'prix': 70.00,
        'disponible': True,
        'image_url': '/Tempura.jpg'
    },
    {
        'nom': 'Yakitori',
        'pays': 'japon',
        'description': 'Grilled chicken skewers with tare sauce',
        'prix': 65.00,
        'disponible': True,
        'image_url': '/Yakitori.jpg'
    },
    {
        'nom': 'Mochi',
        'pays': 'japon',
        'description': 'Sweet rice cake dessert with various fillings',
        'prix': 45.00,
        'disponible': True,
        'image_url': '/Mochi.jpg'
    },
    
    # 🇨🇳 China
    {
        'nom': 'Peking Duck',
        'pays': 'chine',
        'description': 'Roasted duck with pancakes',
        'prix': 150.00,
        'disponible': True,
        'image_url': '/Peking duck.jpg'
    },
    {
        'nom': 'Kung Pao Chicken',
        'pays': 'chine',
        'description': 'Spicy stir-fried chicken with peanuts',
        'prix': 75.00,
        'disponible': True,
        'image_url': '/Kung pao chicken.jpg'
    },
    {
        'nom': 'Sweet and Sour Chicken',
        'pays': 'chine',
        'description': 'Crispy chicken in tangy sauce',
        'prix': 70.00,
        'disponible': True,
        'image_url': '/Sweet and sour chicken.jpg'
    },
    {
        'nom': 'Dim Sum',
        'pays': 'chine',
        'description': 'Assortment of steamed dumplings and buns',
        'prix': 85.00,
        'disponible': True,
        'image_url': '/Dim sum.jpg'
    },
    {
        'nom': 'Chow Mein',
        'pays': 'chine',
        'description': 'Stir-fried noodles with vegetables and chicken',
        'prix': 68.00,
        'disponible': True,
        'image_url': '/Chow mein.jpg'
    },
]

# Clear existing dishes and add new ones
Plat.objects.all().delete()
print("Anciens plats supprimés.")

# Add new dishes
for dish in dishes_data:
    plat = Plat.objects.create(**dish)
    print(f"Créé: {plat.nom} ({plat.pays})")

print(f"\nTotal: {Plat.objects.count()} plats créés avec succès!")
