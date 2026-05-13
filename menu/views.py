from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Plat


# Afficher la liste des plats
def liste_plats(request):

    # Récupérer tous les plats disponibles
    plats = Plat.objects.filter(disponible=True)

    # Transformer les plats en liste JSON
    data = []

    for plat in plats:

        data.append({
            'id': plat.id,
            'nom': plat.nom,
            'description': plat.description,
            'prix': float(plat.prix),
            'disponible': plat.disponible,
        })

    return JsonResponse(data, safe=False)


# Ajouter un plat
def create_plat(request):

    if request.method == 'POST':

        nom = request.POST.get('nom')
        description = request.POST.get('description')
        prix = request.POST.get('prix')

        Plat.objects.create(
            nom=nom,
            description=description,
            prix=prix
        )

        return redirect('plats_list')

    return render(request, 'menu/create.html')


# Modifier un plat
def update_plat(request, plat_id):

    plat = Plat.objects.get(id=plat_id)

    if request.method == 'POST':

        plat.nom = request.POST.get('nom')
        plat.description = request.POST.get('description')
        plat.prix = request.POST.get('prix')

        plat.save()

        return redirect('plats_list')

    return render(request, 'menu/update.html', {
        'plat': plat
    })


# Supprimer un plat
def delete_plat(request, plat_id):

    plat = Plat.objects.get(id=plat_id)

    plat.delete()

    return redirect('plats_list')