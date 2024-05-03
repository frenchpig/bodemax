from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    model = Item
    #importante que serializer contenga todos los campos del modelo.
    #de caso de no ingrearlos estos al momento de guardarlo en.
    #la base de datos genera un "error" y dicho dato no se ingresa.
    fields = ('id','name','price','stock','description','category','user_key')