from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(ExtendedUser)
admin.site.register(Solicitud)
admin.site.register(SolicitudItem)