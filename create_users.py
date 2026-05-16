import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from accounts.models import User

# Create admin user
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser(
        username='admin',
        email='admin@proresto.com',
        password='admin123',
        role='admin'
    )
    print("Admin user created!")

# Create serveur user
if not User.objects.filter(username='serveur').exists():
    serveur = User.objects.create_user(
        username='serveur',
        email='serveur@proresto.com',
        password='serveur123',
        role='serveur'
    )
    print("Serveur user created!")

print("Users created successfully!")
