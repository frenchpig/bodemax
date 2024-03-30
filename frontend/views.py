from django.shortcuts import render
from api.models import Category

# Create your views here.

#definir pagina principal
def loadIndex(request):
  return render(request, 'index.html')

def loadAddProduct(request):
  categories = Category.objects.all()
  return render(request, 'agregar-producto.html', {'categories': categories})

def loadViewProducts(request):
  return render(request, 'ver-productos.html')