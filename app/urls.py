from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('user-detail/<int:pk>', UserDetailView.as_view(), name='user_register'),
    path('list-users/', UserListView.as_view(), name='user_register'),
]
