from rest_framework import serializers
from django.conf import settings
from .models import Categorie, Plat


class PlatSerializer(serializers.ModelSerializer):
    image_display = serializers.SerializerMethodField()

    class Meta:
        model = Plat
        fields = '__all__'

    def get_image_display(self, obj):
        image_url = obj.get_image
        if image_url and image_url.startswith('/'):
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(image_url)
            else:
                return f"http://127.0.0.1:8000{image_url}"
        return image_url


class CategorieSerializer(serializers.ModelSerializer):
    plats = PlatSerializer(many=True, read_only=True)
    
    class Meta:
        model = Categorie
        fields = '__all__'
