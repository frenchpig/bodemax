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
    items = Item.objects.all()
    extendedusers = ExtendedUser.objects.all()
    itemcombined=[]
    for item in items:
      specific_user = extendedusers.get(api_key=item.user_key)
      object = {'item':item,'user':specific_user}
      itemcombined.append(object)
    context = {'items': itemcombined}
    return render(request, 'ver-productos.html', context)
