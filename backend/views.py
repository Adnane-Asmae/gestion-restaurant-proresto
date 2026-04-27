from django.shortcuts import render

# Create your views here.
from menu.models import Plat

def list_plats(request):
    plats = Plat.objects.all()
    return render(request, 'plats.html', {'plats': plats})
