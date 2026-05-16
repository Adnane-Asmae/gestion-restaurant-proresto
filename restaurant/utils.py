import qrcode
from io import BytesIO
from django.core.files import File
from django.conf import settings


def generate_qr_code(table):
    # The URL should point to the frontend menu page, optionally with table ID
    # For now, we'll use localhost:5173 as frontend URL
    frontend_url = getattr(settings, 'FRONTEND_URL', 'http://localhost:5173')
    menu_url = f"{frontend_url}/client-menu/{table.id}/"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)
    
    # Create image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to BytesIO
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    
    # Return as Django File
    return File(buffer, name=f'qr_table_{table.id}.png')
