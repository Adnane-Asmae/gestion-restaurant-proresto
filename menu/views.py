from rest_framework import viewsets
from .models import Plat
from .serializers import PlatSerializer


class PlatViewSet(viewsets.ModelViewSet):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
