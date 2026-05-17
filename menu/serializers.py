from rest_framework import serializers
from .models import Categorie, Plat


class PlatSerializer(serializers.ModelSerializer):
    image_display = serializers.SerializerMethodField()

    class Meta:
        model = Plat
        fields = '__all__'

    def get_image_display(self, obj):
        return obj.get_image


class CategorieSerializer(serializers.ModelSerializer):
    plats = PlatSerializer(many=True, read_only=True)
    
    class Meta:
        model = Categorie
        fields = '__all__'
