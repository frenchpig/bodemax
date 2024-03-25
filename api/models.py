from django.db import models

# Create your models here.
class Category(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)

  def __str__(self):
    txt = "{0} - Nombre: {1}"
    return txt.format(self.id,self.name)
class Item(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  stock = models.IntegerField()
  description = models.TextField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  def __str__(self):
    txt = "{0} - Nombre: {1}, Precio: {2}, Stock: {3}"
    return txt.format(self.id,self.name,self.price,self.stock)
