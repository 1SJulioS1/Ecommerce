
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls'))
]
