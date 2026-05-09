from django.shortcuts import render, redirect
from .models import Commande
from restaurant.models import Table
from menu.models import Plat
from accounts.models import User


def commandes_list(request):
    commandes = Commande.objects.all()
    return render(request, 'orders/list.html', {'commandes': commandes})


def create_commande(request):
    if request.method == 'POST':
        table_id = request.POST.get('table')
        client_id = request.POST.get('client')
        plats_ids = request.POST.getlist('plats')

        table = Table.objects.get(id=table_id)
        client = User.objects.get(id=client_id)

        commande = Commande.objects.create(table=table, client=client)

        for plat_id in plats_ids:
            plat = Plat.objects.get(id=plat_id)
            commande.plats.add(plat)

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

