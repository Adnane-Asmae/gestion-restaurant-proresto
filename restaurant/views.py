from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Table

def liste_tables(request):
    # Récupérer toutes les tables
    tables = Table.objects.all()
    
    # Transformer en liste de dictionnaires
    data = []
    for table in tables:
        data.append({
            'id': table.id,
            'numero': table.numero,
            'capacite': table.capacite,
            'est_occupee': table.est_occupee,
        })
    
    # Retourner en format JSON
    return JsonResponse(data, safe=False)