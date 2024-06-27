from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import json
from django.http import JsonResponse
from django.middleware.csrf import get_token
from api.models import *


# Create your views here.

#definir pagina principal
def loadIndex(request):
  return render(request, 'index.html')

def loadAddProduct(request):
  extended_user = request.user.extendeduser
  if extended_user.role == 'admin':
    extendedusers = ExtendedUser.objects.all()
    context = {'extendedusers':extendedusers,'isAdmin':True}
  if extended_user.role == 'user':
    context = {'isAdmin':False,'api_key':extended_user.api_key}
  print(context)
  return render(request, 'agregar-producto.html',context)

def loadViewProducts(request):
    extended_user = request.user.extendeduser
    if extended_user.role == 'admin':
      items = Item.objects.all()
      extendedusers = ExtendedUser.objects.all()
      itemcombined=[]
      for item in items:
        specific_user = extendedusers.get(api_key=item.user_key)
        object = {'item':item,'user':specific_user}
        itemcombined.append(object)
      context = {'items': itemcombined}
    if extended_user.role == 'user':
      items = Item.objects.filter(user_key=extended_user.api_key)
      itemcombined=[]
      for item in items:
        object = {'item':item,'user':extended_user}
        itemcombined.append(object)
      context = {'items':itemcombined}
    return render(request, 'ver-productos.html', context)

def loadViewSolicitud(request):
    extended_user = request.user.extendeduser
    if extended_user.role == 'admin':
      items = Item.objects.all()
      extendedusers = ExtendedUser.objects.all()
      itemcombined=[]
      for item in items:
        specific_user = extendedusers.get(api_key=item.user_key)
        object = {'item':item,'user':specific_user}
        itemcombined.append(object)
      context = {'items': itemcombined,'api_key':extended_user.api_key}
    if extended_user.role == 'user':
      items = Item.objects.filter(user_key=extended_user.api_key)
      itemcombined=[]
      for item in items:
        object = {'item':item,'user':extended_user}
        itemcombined.append(object)
      context = {'items':itemcombined,'api_key':extended_user.api_key}
    return render(request, 'crear-solicitud.html', context)



def loadViewLogin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username,password=password)
    if user is not None:
      login(request,user)
      return redirect('/')
    else:
      context = {'failedAuth': True}
      return render(request, 'login.html',context)
  if request.method == 'GET':
    context = {'failedAuth': False}
    return render(request, 'login.html',context)
  
def loadViewVerSolicitudes(request):
  extended_user = request.user.extendeduser
  if extended_user.role == 'admin':
    solicitudes=Solicitud.objects.all()
    solicitudes_items=SolicitudItem.objects.all()
    context = {'solicitudes':solicitudes,'solicitudes_items':solicitudes_items,'isAdmin':True}
  if extended_user.role=='user':
    solicitudes=Solicitud.objects.filter(user_key=extended_user.api_key)
    solicitud_items=SolicitudItem.objects.filter(solicitud__in=solicitudes)
    context = {'solicitudes':solicitudes,'solicitudes_items':solicitud_items,'isAdmin':False}
  return render(request, 'ver-solicitudes.html', context)

