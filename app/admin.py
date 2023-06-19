from django.contrib import admin
from .models import CustomUser, Address, Category

# Registra el modelo CustomUser y la clase de administrador personalizada en el sitio de administración
admin.site.register(CustomUser)
admin.site.register(Address)
admin.site.register(Category)
