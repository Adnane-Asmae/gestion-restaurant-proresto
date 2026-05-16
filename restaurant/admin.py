from django.contrib import admin
from django.utils.html import format_html
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ('numero', 'capacite', 'est_occupee', 'qr_code_preview')
    # Filtre par état (occupée ou libre)
    list_filter = ('est_occupee',)
    # Actions
    actions = ['regenerate_qr_codes']
    
    def qr_code_preview(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" style="max-width: 50px; max-height: 50px;" />', obj.qr_code.url)
        return "No QR Code"
    qr_code_preview.short_description = 'QR Code'
    
    def regenerate_qr_codes(self, request, queryset):
        for table in queryset:
            table.regenerate_qr_code()
        self.message_user(request, f"QR codes régénérés pour {queryset.count()} tables.")
    regenerate_qr_codes.short_description = "Régénérer les QR Codes"