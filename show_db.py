
import os
import django

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from menu.models import Plat, Categorie
from restaurant.models import Table
from orders.models import Commande
from accounts.models import User
from chatbot.models import ChatConversation, ChatMessage

print('='*60)
print('  BASE DE DONNÉES PRORESTO')
print('='*60)

print('\n--- UTILISATEURS ---')
users = User.objects.all()
if users:
    for u in users:
        print(f'  ID: {u.id} | Username: {u.username} | Email: {u.email} | Rôle: {u.role}')
else:
    print('  Aucun utilisateur trouvé')

print('\n--- CATÉGORIES ---')
categories = Categorie.objects.all()
if categories:
    for c in categories:
        print(f'  ID: {c.id} | Nom: {c.nom}')
else:
    print('  Aucune catégorie trouvée')

print('\n--- PLATS ---')
plats = Plat.objects.all()
if plats:
    for p in plats:
        print(f'  ID: {p.id} | Nom: {p.nom} | Prix: {p.prix} DH | Disponible: {p.disponible}')
else:
    print('  Aucun plat trouvé')

print('\n--- TABLES ---')
tables = Table.objects.all()
if tables:
    for t in tables:
        etat = "Occupée" if t.est_occupee else "Libre"
        print(f'  ID: {t.id} | Numéro: {t.numero} | Capacité: {t.capacite} | État: {etat}')
else:
    print('  Aucune table trouvée')

print('\n--- COMMANDES ---')
commandes = Commande.objects.all()
if commandes:
    for c in commandes:
        table_num = c.table.numero if c.table else 'N/A'
        print(f'  ID: {c.id} | Table: {table_num} | Statut: {c.statut} | Total: {c.total} DH')
else:
    print('  Aucune commande trouvée')

print('\n--- CONVERSATIONS CHATBOT ---')
conversations = ChatConversation.objects.all()
if conversations:
    for conv in conversations:
        msg_count = conv.messages.count()
        print(f'  ID: {conv.id} | Session: {conv.session_key[:10]}... | Messages: {msg_count}')
else:
    print('  Aucune conversation trouvée')

print('\n' + '='*60)

