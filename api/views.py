from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Item, Category
import json
# Create your views here.
@csrf_exempt
def create_item(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    name = data.get('nombre')
    price = data.get('precio')
    stock = data.get('stock')
    description = data.get('descripcion')
    category_id = data.get('categoria')

    try:
      category = Category.objects.get(id=category_id)
      item = Item.objects.create(
        name = name,
        price = price,
        stock = stock,
        description = description,
        category=category
      )
      return JsonResponse({'mensaje': 'Item creado correctamente!'}, status=201)
    except Category.DoesNotExist:
      return JsonResponse({'error': 'La categoría especificada no existe'}, status=400)
  else:
    return JsonResponse({'error': 'Método no permitido'}, status=405)

@csrf_exempt
def create_category(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    name = data.get('nombre')
    category = Category.objects.create(
      name = name
    )
    return JsonResponse({'mensaje': 'Categoria creada correctamente!'}, status=201)
  else:
    return JsonResponse({'error': 'Metodo no permitido'}, status=405)