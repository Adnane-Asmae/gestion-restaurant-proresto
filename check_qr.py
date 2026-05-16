import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from restaurant.models import Table

tables = Table.objects.all()
for table in tables:
    print(f"Table {table.numero}:")
    print(f"  QR Code: {table.qr_code}")
    print(f"  QR Code URL: {table.qr_code.url if table.qr_code else 'None'}")
