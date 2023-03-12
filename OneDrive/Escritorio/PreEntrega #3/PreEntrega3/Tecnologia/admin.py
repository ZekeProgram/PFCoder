from django.contrib import admin
from .models import Computadores, Televisores, Telefonos

# Register your models here.

admin.site.register(Computadores)
admin.site.register(Televisores)
admin.site.register(Telefonos)