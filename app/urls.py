from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('user-detail/', UserDetailView.as_view(), name='user_register'),
]
