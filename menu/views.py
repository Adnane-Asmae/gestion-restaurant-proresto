
import json
import logging
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Categorie, Plat

logger = logging.getLogger(__name__)


def get_plat_dict(plat, request=None):
    """Convert Plat object to dictionary"""
    data = {
        'id': plat.id,
        'nom': plat.nom,
        'description': plat.description,
        'prix': float(plat.prix),
        'disponible': plat.disponible,
        'pays': plat.pays,
        'categorie_id': plat.categorie_id,
        'image_url': plat.image_url,
    }
    
    # Add image_display
    image_url = plat.get_image
    if image_url:
        if image_url.startswith('/'):
            if request:
                data['image_display'] = request.build_absolute_uri(image_url)
            else:
                data['image_display'] = f"http://127.0.0.1:8000{image_url}"
        else:
            data['image_display'] = image_url
    else:
        data['image_display'] = None
    
    return data


def get_categorie_dict(categorie):
    """Convert Categorie object to dictionary"""
    return {
        'id': categorie.id,
        'nom': categorie.nom,
    }


@require_http_methods(["GET"])
def categories_list(request):
    """Get all categories"""
    try:
        categories = Categorie.objects.all()
        data = [get_categorie_dict(cat) for cat in categories]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting categories: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def categories_detail(request, pk):
    """Get single category"""
    try:
        categorie = Categorie.objects.get(pk=pk)
        return JsonResponse(get_categorie_dict(categorie))
    except Categorie.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    except Exception as e:
        logger.error(f"Error getting category {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def plats_list(request):
    """Get all plats"""
    try:
        plats = Plat.objects.all()
        data = [get_plat_dict(plat, request) for plat in plats]
        return JsonResponse(data, safe=False)
    except Exception as e:
        logger.error(f"Error getting plats: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@require_http_methods(["GET"])
def plats_detail(request, pk):
    """Get single plat"""
    try:
        plat = Plat.objects.get(pk=pk)
        return JsonResponse(get_plat_dict(plat, request))
    except Plat.DoesNotExist:
        return JsonResponse({'error': 'Dish not found'}, status=404)
    except Exception as e:
        logger.error(f"Error getting dish {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def categories_create(request):
    """Create new category"""
    try:
        data = json.loads(request.body)
        categorie = Categorie.objects.create(nom=data.get('nom', ''))
        return JsonResponse(get_categorie_dict(categorie), status=201)
    except Exception as e:
        logger.error(f"Error creating category: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def categories_update(request, pk):
    """Update category"""
    try:
        categorie = Categorie.objects.get(pk=pk)
        data = json.loads(request.body)
        if 'nom' in data:
            categorie.nom = data['nom']
        categorie.save()
        return JsonResponse(get_categorie_dict(categorie))
    except Categorie.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating category {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def categories_delete(request, pk):
    """Delete category"""
    try:
        categorie = Categorie.objects.get(pk=pk)
        categorie.delete()
        return JsonResponse({'message': 'Category deleted successfully'}, status=204)
    except Categorie.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    except Exception as e:
        logger.error(f"Error deleting category {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["POST"])
def plats_create(request):
    """Create new plat"""
    try:
        data = json.loads(request.body)
        
        plat = Plat.objects.create(
            nom=data.get('nom', ''),
            description=data.get('description', ''),
            prix=data.get('prix', 0),
            disponible=data.get('disponible', True),
            pays=data.get('pays', ''),
            categorie_id=data.get('categorie'),
            image_url=data.get('image_url', ''),
        )
        return JsonResponse(get_plat_dict(plat, request), status=201)
    except Exception as e:
        logger.error(f"Error creating dish: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["PUT", "PATCH"])
def plats_update(request, pk):
    """Update plat"""
    try:
        plat = Plat.objects.get(pk=pk)
        data = json.loads(request.body)
        
        if 'nom' in data:
            plat.nom = data['nom']
        if 'description' in data:
            plat.description = data['description']
        if 'prix' in data:
            plat.prix = data['prix']
        if 'disponible' in data:
            plat.disponible = data['disponible']
        if 'pays' in data:
            plat.pays = data['pays']
        if 'categorie' in data:
            plat.categorie_id = data['categorie']
        if 'image_url' in data:
            plat.image_url = data['image_url']
        
        plat.save()
        return JsonResponse(get_plat_dict(plat, request))
    except Plat.DoesNotExist:
        return JsonResponse({'error': 'Dish not found'}, status=404)
    except Exception as e:
        logger.error(f"Error updating dish {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt
@require_http_methods(["DELETE"])
def plats_delete(request, pk):
    """Delete plat"""
    try:
        plat = Plat.objects.get(pk=pk)
        plat.delete()
        return JsonResponse({'message': 'Dish deleted successfully'}, status=204)
    except Plat.DoesNotExist:
        return JsonResponse({'error': 'Dish not found'}, status=404)
    except Exception as e:
        logger.error(f"Error deleting dish {pk}: {e}")
        return JsonResponse({'error': str(e)}, status=500)

