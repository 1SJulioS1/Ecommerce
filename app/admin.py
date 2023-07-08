from django.contrib import admin
from .models import *

# Registra el modelo CustomUser y la clase de administrador personalizada en el sitio de administración
admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
