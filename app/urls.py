from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import *

urlpatterns = [
    # user management
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('user-detail/<int:pk>', UserDetailView.as_view(), name='user_register'),
    path('list-users/', UserListView.as_view(), name='user_register'),

    # category management
    path("category/", CategoryView.as_view(), name="category"),
]
