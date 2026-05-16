import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from accounts.models import User

def create_users():
    # Create admin user
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@proresto.com',
            password='admin123',
            role='admin'
        )
        print("Admin user created!")
    else:
        print("Admin user already exists!")

    # Create serveur user
    if not User.objects.filter(username='serveur').exists():
        serveur = User.objects.create_user(
            username='serveur',
            email='serveur@proresto.com',
            password='serveur123',
            role='serveur'
        )
        serveur.is_staff = True
        serveur.save()
        print("Serveur user created!")
    else:
        print("Serveur user already exists!")

    # Create cuisinier user
    if not User.objects.filter(username='cuisinier').exists():
        cuisinier = User.objects.create_user(
            username='cuisinier',
            email='cuisinier@proresto.com',
            password='cuisinier123',
            role='cuisinier'
        )
        cuisinier.is_staff = True
        cuisinier.save()
        print("Cuisinier user created!")
    else:
        print("Cuisinier user already exists!")

if __name__ == '__main__':
    create_users()
