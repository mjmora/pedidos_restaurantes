from django.contrib import admin

from manejo_pedidos.models import *
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Consumo)
admin.site.register(Menu)
admin.site.register(Mesa)
admin.site.register(Pedido)
admin.site.register(Persona)
admin.site.register(Personal)