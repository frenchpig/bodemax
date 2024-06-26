from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#Debido a que cada llave de la api esta asociada a un usuario se tuvo que extender el modelo de usario para permitir el nuevo campo llamado api_key
class ExtendedUser(models.Model):
  ROLE_CHOICES = [
    ('user','user'),
    ('admin','admin'),
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  api_key = models.CharField(max_length=8,unique=True,blank=True)
  role = models.CharField(max_length=5,choices=ROLE_CHOICES,default='user')

  def save(self, *args, **kwargs):
    if not self.api_key:
      self.api_key = self.generate_unique_api_key()
    super().save(*args, **kwargs)

  def generate_unique_api_key(self):
    unique_key = None
    while not unique_key:
      potential_key = get_random_string(length=8, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
      if not ExtendedUser.objects.filter(api_key=potential_key).exists():
        unique_key = potential_key
    return unique_key
#El siguiente codigo solamente espera atento a la accion de la tabla USER, en el momento de que se genere un
#User nuevo la tabla extender user creara tambien una fila nueva vinculando el usuario recien creado a
#una api key la cual se generara automaticamente con la logica dentro de ExtendedUser
@receiver(post_save, sender=User)
def create_extendeduser(sender, instance, created, **kwargs):
    if created:
        ExtendedUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_extendeduser(sender, instance, **kwargs):
    instance.extendeduser.save()

#Tabla de items

class Item(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  stock = models.IntegerField()
  description = models.TextField()
  category = models.CharField(max_length=30, null=True)
  user_key = models.CharField(max_length=8, default='AABB00')
  def __str__(self):
    txt = "{0} - Nombre: {1}, Precio: {2}, Stock: {3}"
    return txt.format(self.id,self.name,self.price,self.stock)
  
# Tabla de solicitud

class Solicitud(models.Model):
  id = models.AutoField(primary_key=True)
  size = models.CharField(max_length=10)
  items = models.ManyToManyField(Item, through='SolicitudItem')

class SolicitudItem(models.Model):
  solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  amount = models.IntegerField()
