from django.shortcuts import render, redirect
from .models import Commande
from restaurant.models import Table
from menu.models import Plat
from accounts.models import User


# Afficher toutes les commandes
def commandes_list(request):

    commandes = Commande.objects.all()

    return render(request, 'orders/list.html', {
        'commandes': commandes
    })


# Créer une nouvelle commande
def create_commande(request):

    if request.method == 'POST':

        table_id = request.POST.get('table')
        client_id = request.POST.get('client')
        plats_ids = request.POST.getlist('plats')

        table = Table.objects.get(id=table_id)
        client = User.objects.get(id=client_id)

        # Création de la commande
        commande = Commande.objects.create(
            table=table,
            client=client
        )

        # Ajouter les plats à la commande
        for plat_id in plats_ids:

            plat = Plat.objects.get(id=plat_id)

            commande.plats.add(plat)

        # Calcul automatique du total
        commande.calculate_total()

        return redirect('commandes_list')

    tables = Table.objects.all()
    clients = User.objects.filter(role='client')
    plats = Plat.objects.all()

    return render(request, 'orders/create.html', {
        'tables': tables,
        'clients': clients,
        'plats': plats
    })


# Modifier le statut d'une commande
def modifier_commande(request, commande_id):

    commande = Commande.objects.get(id=commande_id)

    if request.method == 'POST':

        nouveau_statut = request.POST.get('statut')

        commande.statut = nouveau_statut

        commande.save()

        return redirect('commandes_list')

    return render(request, 'orders/modifier.html', {
        'commande': commande
    })