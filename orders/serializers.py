from rest_framework import serializers
from .models import Commande
from menu.serializers import PlatSerializer
from restaurant.serializers import TableSerializer


class CommandeSerializer(serializers.ModelSerializer):
    plats = PlatSerializer(many=True, read_only=True)
    table = TableSerializer(read_only=True)
    
    class Meta:
        model = Commande
        fields = '__all__'
