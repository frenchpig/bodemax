from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Item, ExtendedUser, Solicitud, SolicitudItem
from .serializers import ItemSerializer, SolicitudSerializer
import json
# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
  queryset=Item.objects.all()
  serializer_class = ItemSerializer

  #POST
  #define que se realizara al momento de utilizar metodo POST
  #deberia agregar un item a la base de datos
  def create(self,request,*args,**kwargs):
    #recupera la api_key enviada por el usuario
    api_key = request.data.get('user_key',None)
    if api_key is None:
      return Response({'error':'apy_key is required'}, status=status.HTTP_400_BAD_REQUEST)
    #comprueba si la api_key es valida
    extended_user = ExtendedUser.objects.filter(api_key=api_key).first()
    if extended_user is None:
      return Response({'error': 'Invalid api_key'}, status=status.HTTP_403_FORBIDDEN)
    #en caso de que no haya errores en los datos ingresados guarda los datos
    return super().create(request,*args,**kwargs)
  
  #GET
  #define que se realizara al momento de utilizar metodo GET
  #deberia retornar todos los items de cierto usuario
  def list(self, request, *args, **kwargs):
    #recupera la api key recepcionada comprobando de que exista
    api_key = request.GET.get('user_key',None)
    if api_key is None:
      return Response({'error': 'api_key required'}, status=status.HTTP_400_BAD_REQUEST)
    #comprueba la valides de dicha api key con datos de la BBDD
    extended_user = ExtendedUser.objects.filter(api_key=api_key).first()
    if extended_user is None:
      return Response({'error': 'Invalid api_key'}, status=status.HTTP_403_FORBIDDEN)
    #configura la solicitud a la BBDD y retorna la respuesta de esta.
    queryset = self.queryset.filter(user_key=api_key)
    serializer = self.serializer_class(queryset,many=True)
    return Response(serializer.data)
  
  # PATCH (Importante que el metodo sea este debido a que por definicion es el que es necesario, ademas que por su metodo de implementacion es el que se necesita.)
  #define que se realizara al momento de utilizar metodo PUT
  #deberia actualizar un item solo si es del usuario
  def update(self,request,*args,**kwargs):
    item_id = kwargs.get('pk')
    api_key = request.data.get('user_key',None)
    if api_key is None:
      return Response({'error': 'user_key is required'}, status=status.HTTP_400_BAD_REQUEST)
    user = ExtendedUser.objects.filter(api_key=api_key).first()
    if user is None:
      return Response({'error': 'Invalid user_key'}, status=status.HTTP_403_FORBIDDEN)
    item = self.queryset.get(pk=item_id)
    if item.user_key!=api_key:
      return Response({'error': 'Item doesnt belong to user'}, status=status.HTTP_403_FORBIDDEN)
    return super().update(request, *args, **kwargs)
  
  def destroy(self,request,*args,**kwargs):
    api_key = request.GET.get('user_key',None)
    if api_key is None:
      return Response({'error': 'user_key is required'}, status=status.HTTP_400_BAD_REQUEST)
    user = ExtendedUser.objects.filter(api_key=api_key).first()
    if user is None:
      return Response({'error': 'Invalid user_key'}, status=status.HTTP_403_FORBIDDEN)
    instance = self.get_object()
    if instance.user_key != api_key:
      return Response({'error': 'this item doenst belong to you'}, status=status.HTTP_403_FORBIDDEN)
    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)


class SolicitudViewSet(viewsets.ModelViewSet):
  queryset=Solicitud.objects.all()
  serializer_class = SolicitudSerializer

  # Metodo POST
  def create(self,request,*args,**kwargs):
    data = request.data
    api_key = data[1]["api_key"]
    solicitud_data = data[0]["solicitud"]
    cantidad = 0
    for item_data  in solicitud_data:
      item = Item.objects.get(id=item_data["id"])
      if item.stock<item_data['amount']:
        return Response({'error':f'Se solicitaron mas {item_data["name"]} de los que se encuentran en stock'})
      cantidad += item_data["amount"]
    print(cantidad)
    if cantidad == 1:
      size = 'S'
    if cantidad >= 2:
      size = 'M'
    if cantidad >= 6:
      size = 'L'
    if cantidad>10:
      size = 'XL'
    solicitud = Solicitud.objects.create(size=size,user_key=api_key)
    for item_data in solicitud_data:
      item = Item.objects.get(id=item_data["id"])
      item.stock = item.stock - item_data['amount']
      item.save()
      SolicitudItem.objects.create(solicitud=solicitud,item=item,amount=item_data["amount"])
    return Response({'message':'Solicitud Creada'})
  
  def destroy(self, request, *args, **kwargs):
    # Obtener la id de la solicitud de los argumentos de la función
    solicitud_id = self.kwargs['pk']
    # Obtener la api_key del cuerpo de la solicitud
    api_key = request.data.get('api_key', None)

    # Comprobar si la api_key fue proporcionada
    if api_key is None:
        return Response({'error': 'api_key is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Intentar obtener la solicitud con la id y la api_key proporcionadas
        solicitud = Solicitud.objects.get(id=solicitud_id, user_key=api_key)
        # Si la solicitud existe y corresponde a la api_key, eliminarla
        solicitud.delete()
        return Response({'message': 'Solicitud eliminada correctamente'}, status=status.HTTP_200_OK)
    except Solicitud.DoesNotExist:
        # Si la solicitud no existe, devolver un error
        return Response({'error': 'Solicitud no encontrada'}, status=status.HTTP_404_NOT_FOUND)
    

def create_solicitud(request):
  if request.method == 'POST':
    print('POSTING')
    return JsonResponse({'message':'WIP'})
  return JsonResponse({'message':'WIP'})

def create_item(request):
    # Lógica para crear un ítem
    return JsonResponse({'message': 'Item created successfully'})

def create_category(request):
    # Lógica para crear un ítem
    return JsonResponse({'message': 'Item created successfully'})