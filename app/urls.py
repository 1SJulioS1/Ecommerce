from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import *
from .swagger import get_schema_view
from rest_framework import permissions
schema_view = get_schema_view(
    openapi.Info(
        title="Torresuelto webpage API",
        default_version='v1',
        description="Test API",
        contact=openapi.Contact(email="sjsiless@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),


    # user management
    path("login/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', UserRegistrationView.as_view(), name='user_register'),
    path('users/admin/', AdminRegistrationView.as_view(), name='admin_register'),
    path("users/me/", UserDetailView.as_view(), name="user-list-edit"),
    path("logout/", UserLogoutView.as_view(), name=""),
    path('users/list', UserListView.as_view(), name='user_register'),


    # category management
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/create/", CategoryCreateView.as_view(), name="category_create"),
    path("category/<slug:slug>",
         CategoryDetailUpdateDeleteView.as_view(), name="category_detail_update_remove"),

    # product management
    path("product/", ProductListView.as_view(), name="product_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<slug:slug>",
         ProductView.as_view(), name="category_detail_update_remove"),
    path("product/detail/<slug:slug>",
         ProductDetailView.as_view(), name="product_detail"),

    # Cart CRUD
    path("cart/", CartView.as_view(), name="cart-view"),

    # Courier CRUD
    path("courier/", CourierListCreateView.as_view(), name="courier_list_create"),
    path("courier/<int:pk>", CourierDetailUpdateDeleteView.as_view(),
         name="courier_list_create"),

    # Order view
    path("order/me/", OrderView.as_view(), name="order_user_view"),
    path("order/<int:pk>", OrderUpdateView.as_view(), name="order_update"),
    path("order/", OrderListView.as_view(), name="order_list")
]
