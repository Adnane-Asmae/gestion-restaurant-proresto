from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Table


# Afficher la liste des tables
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


# Modifier l'état d'une table (libre/occupée)
def modifier_table(request, table_id):

    table = Table.objects.get(id=table_id)

    # Inverser l'état
    table.est_occupee = not table.est_occupee

    table.save()

    return redirect('tables_list')