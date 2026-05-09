from django.http import JsonResponse
from .models import Plat

def liste_plats(request):
    # Récupérer tous les plats disponibles dans la base de données
    plats = Plat.objects.filter(disponible=True)
    
    # Transformer les plats en liste de dictionnaires
    # pour pouvoir les envoyer en JSON
    data = []
    for plat in plats:
        data.append({
            'id': plat.id,
            'nom': plat.nom,
            'description': plat.description,
            'prix': float(plat.prix),      # Convertir Decimal en float pour JSON
            'disponible': plat.disponible,
        })
    
    # Retourner la liste en format JSON
    return JsonResponse(data, safe=False)