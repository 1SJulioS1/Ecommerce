from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path
from .views import *

urlpatterns = [
    # user management
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_register'),
    path('users/', UserListView.as_view(), name='user_register'),

    # category management
    path("category/", CategoryListView.as_view(), name="category_list_create"),
    path("category/<slug:slug>",
         CategoryView.as_view(), name="category_detail"),

    # product management
    path("product/", ProductDetailView.as_view(), name="product_list_create"),
    path("product-update/<slug:slug>",
         ProductView.as_view(), name="product_update"),
    path("product/<slug:slug>",
         ProductListView.as_view(), name="product_list"),



]
