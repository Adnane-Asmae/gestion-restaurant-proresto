
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Plat

# Sample dishes data with REAL meal photos
dishes_data = [
    # 🇲🇦 Morocco
    {
        'nom': 'Tagine',
        'pays': 'maroc',
        'description': 'Traditional Moroccan tagine of lamb with dried fruits and nuts',
        'prix': 85.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Moroccan%20tagine%20with%20lamb%2C%20prunes%2C%20apricots%2C%20almonds%2C%20cinnamon%2C%20traditional%20clay%20pot%2C%20rustic%20wooden%20table%2C%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Couscous',
        'pays': 'maroc',
        'description': 'Traditional Friday special with vegetables and meat',
        'prix': 95.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Moroccan%20couscous%20with%20chicken%2C%20carrots%2C%20zucchini%2C%20potatoes%2C%20chickpeas%2C%20traditional%20serving%20dish%2C%20mint%20tea%20glasses%2C%20golden%20tray%2C%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Pastilla',
        'pays': 'maroc',
        'description': 'Sweet/savory pie with chicken, almonds, and cinnamon',
        'prix': 75.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Moroccan%20pastilla%20pie%20with%20almonds%2C%20powdered%20sugar%2C%20cinnamon%2C%20traditional%20serving%2C%20moroccan%20architecture%20background%2C%20high%20quality%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Harira',
        'pays': 'maroc',
        'description': 'Famous traditional soup with lentils and meat',
        'prix': 45.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Moroccan%20harira%20soup%20in%20traditional%20ceramic%20bowl%2C%20with%20moroccan%20tea%20pot%2C%20msemen%20bread%2C%20dates%2C%20professional%20food%20photography&image_size=square_hd'
    },
    
    # 🇪🇸 Spain
    {
        'nom': 'Paella',
        'pays': 'espagne',
        'description': 'Most iconic Spanish dish with rice, saffron, and seafood',
        'prix': 98.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Spanish%20paella%20seafood%20in%20traditional%20pan%2C%20shrimp%2C%20mussels%2C%20lemon%2C%20saffron%20rice%2C%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Tortilla Española',
        'pays': 'espagne',
        'description': 'Classic Spanish potato omelette',
        'prix': 55.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Spanish%20tortilla%20espa%C3%B1ola%20potato%20omelette%2C%20golden%20brown%2C%20parsley%20garnish%2C%20sliced%2C%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Patatas Bravas',
        'pays': 'espagne',
        'description': 'Fried potatoes with spicy tomato sauce',
        'prix': 48.00,
        'disponible': True,
        'image': 'https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=Spanish%20patatas%20bravas%20fried%20potatoes%20with%20spicy%20tomato%20sauce%20and%20aioli%2C%20parsley%20garnish%2C%20professional%20food%20photography&image_size=square_hd'
    },
    {
        'nom': 'Gazpacho',
        'pays': 'espagne',
        'description': 'Cold tomato soup perfect for summer',
        'prix': 52.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?q=80&w=800&auto=format&fit=crop'
    },
    
    # 🇮🇹 Italy
    {
        'nom': 'Pizza Margherita',
        'pays': 'italie',
        'description': 'Classic pizza with tomato, mozzarella, and fresh basil',
        'prix': 72.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Pasta Carbonara',
        'pays': 'italie',
        'description': 'Creamy pasta with pancetta, eggs, and pecorino',
        'prix': 78.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1612874742237-6526221588e3?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Lasagna',
        'pays': 'italie',
        'description': 'Layered pasta with bolognese and bechamel sauce',
        'prix': 85.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1574894709920-11b28e7367e3?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Risotto',
        'pays': 'italie',
        'description': 'Creamy rice with mushrooms and parmesan',
        'prix': 82.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Tiramisu',
        'pays': 'italie',
        'description': 'Classic Italian dessert with coffee and mascarpone',
        'prix': 48.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?q=80&w=800&auto=format&fit=crop'
    },
    
    # 🇨🇳 China
    {
        'nom': 'Peking Duck',
        'pays': 'chine',
        'description': 'Famous roasted duck with pancakes and hoisin sauce',
        'prix': 160.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1518492104633-130d0cc84637?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Dim Sum',
        'pays': 'chine',
        'description': 'Assortment of steamed dumplings and buns',
        'prix': 85.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Kung Pao Chicken',
        'pays': 'chine',
        'description': 'Spicy stir-fried chicken with peanuts and vegetables',
        'prix': 75.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1525755662778-989d0524087e?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Sweet and Sour Chicken',
        'pays': 'chine',
        'description': 'Crispy chicken in tangy sweet and sour sauce',
        'prix': 72.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Chow Mein',
        'pays': 'chine',
        'description': 'Stir-fried noodles with vegetables and chicken',
        'prix': 68.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=800&auto=format&fit=crop'
    },
    
    # 🇯🇵 Japan
    {
        'nom': 'Sushi',
        'pays': 'japon',
        'description': 'Fresh assorted sushi and sashimi platter',
        'prix': 120.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1579871494447-9811cf80d66c?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Ramen',
        'pays': 'japon',
        'description': 'Rich tonkotsu broth with noodles and chashu',
        'prix': 88.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Tempura',
        'pays': 'japon',
        'description': 'Lightly battered and fried seafood and vegetables',
        'prix': 75.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1615361200141-f45040f367be?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Yakitori',
        'pays': 'japon',
        'description': 'Grilled chicken skewers with tare sauce',
        'prix': 65.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1555126634-323283e090fa?q=80&w=800&auto=format&fit=crop'
    },
    {
        'nom': 'Mochi',
        'pays': 'japon',
        'description': 'Sweet rice cake dessert with various fillings',
        'prix': 45.00,
        'disponible': True,
        'image': 'https://images.unsplash.com/photo-1585225654619-c0c87a3c906f?q=80&w=800&auto=format&fit=crop'
    }
]

# Clear existing dishes and add new ones
Plat.objects.all().delete()
print("Anciens plats supprimés.")

# Add new dishes
for dish in dishes_data:
    plat = Plat.objects.create(**dish)
    print(f"Créé: {plat.nom} ({plat.pays})")

print(f"\nTotal: {Plat.objects.count()} plats créés avec succès!")
