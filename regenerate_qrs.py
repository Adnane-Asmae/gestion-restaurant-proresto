import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'resto_project.settings')
django.setup()

from restaurant.models import Table

tables = Table.objects.all()
for table in tables:
    if not table.qr_code:
        table.save()
        print(f"QR code generated for Table {table.numero}")

print("QR code generation complete!")
