
import json
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Commande
from menu.models import Plat
from restaurant.models import Table
from menu.views import get_plat_dict
from restaurant.views import get_table_dict

logger = logging.getLogger(__name__)


def get_commande_dict(commande, request=None):
    """Convert Commande object to dictionary"""
    plats_data = []
    for plat in commande.plats.all():
        plats_data.append(get_plat_dict(plat, request))
        
    table_data = None
    if commande.table:
        table_data = get_table_dict(commande.table, request)
        
    return {
        'id': commande.id,
        'table_id': commande.table_id,
        'table': table_data,
        'plats': plats_data,
        'statut': commande.statut,
        'date_creation': commande.date_creation.isoformat(),
        'heure_creation': commande.heure_creation.isoformat() if commande.heure_creation else None,
        'total': float(commande.total) if commande.total else 0,
        'notes': commande.notes,
    }


@require_http_methods(["GET"])
def commandes_list(request):
    """Get all orders"""
    try:
        commandes = Commande.objects.all()
        data = [get_commande_dict(commande, request) for commande in commandes]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting orders: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def commandes_detail(request, pk):
    """Get single order"""
    try:
        commande = Commande.objects.get(pk=pk)
        return JsonResponse(get_commande_dict(commande, request))
    except Commande.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        logger.error(f"Error getting order {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def commandes_create(request):
    """Create new order"""
    try:
        data = json.loads(request.body)
        
        table = None
        if 'table' in data:
            try:
                table = Table.objects.get(pk=data['table'])
            except Table.DoesNotExist:
                pass
                
        commande = Commande.objects.create(
            table=table,
            statut=data.get('statut', 'en_attente'),
            notes=data.get('notes', ''),
            total=data.get('total', 0),
        )
        
        if 'plats' in data:
            for plat_id in data['plats']:
                try:
                    plat = Plat.objects.get(pk=plat_id)
                    commande.plats.add(plat)
                except Plat.DoesNotExist:
                    continue
        
        return JsonResponse(get_commande_dict(commande, request), status=201)
    except Exception as e:
        logger.error(f"Error creating order: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def commandes_update(request, pk):
    """Update order"""
    try:
        commande = Commande.objects.get(pk=pk)
        data = json.loads(request.body)
        
        if 'table' in data:
            try:
                table = Table.objects.get(pk=data['table'])
                commande.table = table
            except Table.DoesNotExist:
                pass
                
        if 'statut' in data:
            commande.statut = data['statut']
        if 'notes' in data:
            commande.notes = data['notes']
        if 'total' in data:
            commande.total = data['total']
            
        if 'plats' in data:
            commande.plats.clear()
            for plat_id in data['plats']:
                try:
                    plat = Plat.objects.get(pk=plat_id)
                    commande.plats.add(plat)
                except Plat.DoesNotExist:
                    continue
        
        commande.save()
        return JsonResponse(get_commande_dict(commande, request))
    except Commande.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating order {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def commandes_delete(request, pk):
    """Delete order"""
    try:
        commande = Commande.objects.get(pk=pk)
        commande.delete()
        return JsonResponse({'message': 'Order deleted successfully'}, status=204)
    except Commande.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)
    except Exception as e:
        logger.error(f"Error deleting order {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)

