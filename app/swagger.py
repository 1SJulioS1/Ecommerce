from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info = openapi.Info(
    title='My API',
    default_version='v1',
    description='Descripción de mi API',
    contact=openapi.Contact(email='contact@example.com'),
    license=openapi.License(name='MIT License'),
)
schema_view = get_schema_view(
    api_info,
    public=True,
    permission_classes=(permissions.AllowAny,),
)
