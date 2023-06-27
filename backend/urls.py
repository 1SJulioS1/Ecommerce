
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='API Documentation')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),
    path("api/docs", schema_view, name="")
]
