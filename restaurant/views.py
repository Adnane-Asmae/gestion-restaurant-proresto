
import json
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Table, CallServer

logger = logging.getLogger(__name__)


def get_table_dict(table, request=None):
    """Convert Table object to dictionary"""
    data = {
        'id': table.id,
        'numero': table.numero,
        'capacite': table.capacite,
        'est_occupee': table.est_occupee,
    }
    
    if table.qr_code:
        if request:
            data['qr_code_url'] = request.build_absolute_uri(table.qr_code.url)
        else:
            data['qr_code_url'] = f'http://127.0.0.1:8000{table.qr_code.url}'
    else:
        data['qr_code_url'] = None
        
    return data


def get_call_dict(call):
    """Convert CallServer object to dictionary"""
    return {
        'id': call.id,
        'table_id': call.table_id,
        'table_numero': call.table.numero if call.table else None,
        'statut': call.statut,
        'date_creation': call.date_creation.isoformat(),
        'date_resolution': call.date_resolution.isoformat() if call.date_resolution else None,
    }


@require_http_methods(["GET"])
def tables_list(request):
    """Get all tables"""
    try:
        tables = Table.objects.all()
        data = [get_table_dict(table, request) for table in tables]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting tables: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def tables_detail(request, pk):
    """Get single table"""
    try:
        table = Table.objects.get(pk=pk)
        return JsonResponse(get_table_dict(table, request))
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)
    except Exception as e:
        logger.error(f"Error getting table {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def tables_create(request):
    """Create new table"""
    try:
        data = json.loads(request.body)
        table = Table.objects.create(
            numero=data.get('numero'),
            capacite=data.get('capacite', 2),
            est_occupee=data.get('est_occupee', False),
        )
        return JsonResponse(get_table_dict(table, request), status=201)
    except Exception as e:
        logger.error(f"Error creating table: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def tables_update(request, pk):
    """Update table"""
    try:
        table = Table.objects.get(pk=pk)
        data = json.loads(request.body)
        
        if 'numero' in data:
            table.numero = data['numero']
        if 'capacite' in data:
            table.capacite = data['capacite']
        if 'etat' in data:
            table.etat = data['etat']
        if 'est_occupee' in data:
            table.est_occupee = data['est_occupee']
        
        table.save()
        return JsonResponse(get_table_dict(table, request))
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating table {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def tables_delete(request, pk):
    """Delete table"""
    try:
        table = Table.objects.get(pk=pk)
        table.delete()
        return JsonResponse({'message': 'Table deleted successfully'}, status=204)
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)
    except Exception as e:
        logger.error(f"Error deleting table {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def tables_regenerate_qr(request, pk):
    """Regenerate QR code for table"""
    try:
        table = Table.objects.get(pk=pk)
        table.regenerate_qr_code()
        return JsonResponse(get_table_dict(table, request))
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)
    except Exception as e:
        logger.error(f"Error regenerating QR for table {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def calls_list(request):
    """Get all calls"""
    try:
        calls = CallServer.objects.all().order_by('-date_creation')
        data = [get_call_dict(call) for call in calls]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting calls: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def calls_resolve(request, pk):
    """Resolve a call"""
    try:
        call = CallServer.objects.get(pk=pk)
        call.statut = 'resolved'
        call.date_resolution = timezone.now()
        call.save()
        return JsonResponse(get_call_dict(call))
    except CallServer.DoesNotExist:
        return JsonResponse({'error': 'Call not found'}, status=404)
    except Exception as e:
        logger.error(f"Error resolving call {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def create_call_server(request):
    """Create a new call to server"""
    try:
        data = json.loads(request.body)
        table_id = data.get('table_id')
        table = Table.objects.get(id=table_id)
        call = CallServer.objects.create(table=table)
        return JsonResponse(get_call_dict(call), status=201)
    except Table.DoesNotExist:
        return JsonResponse({'error': 'Table not found'}, status=404)
    except Exception as e:
        logger.error(f"Error creating call: {e}")
        return JsonResponse({'error': str(e)}, status=500)

