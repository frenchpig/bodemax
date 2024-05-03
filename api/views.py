from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .models import Item, ExtendedUser
from .serializers import ItemSerializer
import json
# Create your views here.

class ItemViewSet(viewsets.ModelViewSet):
  queryset=Item.objects.all()
  serializer_class = ItemSerializer

  #POST
  #define que se realizara al momento de utilizar metodo POST
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



def create_item(request):
    # Lógica para crear un ítem
    return JsonResponse({'message': 'Item created successfully'})

def create_category(request):
    # Lógica para crear un ítem
    return JsonResponse({'message': 'Item created successfully'})