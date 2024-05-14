from django.shortcuts import render
from api.models import *

# Create your views here.

#definir pagina principal
def loadIndex(request):
  return render(request, 'index.html')

def loadAddProduct(request):
  extendedusers = ExtendedUser.objects.all()
  context = {'extendedusers':extendedusers}
  return render(request, 'agregar-producto.html',context)

def loadViewProducts(request):
  return render(request, 'ver-productos.html')