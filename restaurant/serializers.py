from rest_framework import serializers
from .models import Table, CallServer


class TableSerializer(serializers.ModelSerializer):
    qr_code_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Table
        fields = '__all__'
        extra_fields = ['qr_code_url']
    
    def get_qr_code_url(self, obj):
        if obj.qr_code:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.qr_code.url)
            return f'http://127.0.0.1:8000{obj.qr_code.url}'
        return None


class CallServerSerializer(serializers.ModelSerializer):
    table_numero = serializers.CharField(source='table.numero', read_only=True)
    
    class Meta:
        model = CallServer
        fields = '__all__'
