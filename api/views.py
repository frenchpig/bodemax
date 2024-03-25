from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Item
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
    item = Item.objects.create(
      name = name,
      price = price,
      stock = stock,
      description = description
    )
    return JsonResponse({'mensaje': 'Item creado correctamente!'}, status=201)
  else:
    return JsonResponse({'error': 'Método no permitido'}, status=405)