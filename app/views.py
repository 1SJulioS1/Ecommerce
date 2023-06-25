from .models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes


from django.shortcuts import get_object_or_404


from app.serializers import *
from app.permissions import *
from app.models import *


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = request.data.copy()
        data['user_type'] = 'regular_user'
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()

            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            response_data = {
                'refresh_token': str(refresh_token),
                'access_token': str(access_token),
            }

            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


class AdminRegistrationView(APIView):
    permission_classes = [IsAdmin]

    def post(self, request):
        data = request.data.copy()
        data['user_type'] = 'admin'
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()

            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            response_data = {
                'refresh_token': str(refresh_token),
                'access_token': str(access_token),
            }

            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


class UserDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['usernname']


class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    lookup_field = 'slug'


class CategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
    lookup_field = 'slug'


class ProductDetailView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    ordering_fields = ['name', 'category', 'price']
    lookup_field = 'slug'


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category', 'price']
    ordering_fields = ['name', 'category', 'price']
    lookup_field = 'slug'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')

    try:
        product = Product.objects.get(pk=product_id)

        # Verificar si el usuario tiene un carrito asociado
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            # Si el usuario no tiene un carrito, crear uno nuevo y asociarlo al usuario
            cart = Cart.objects.create(user=request.user)

        # Verificar si el producto ya existe en el carrito
        cart_item = CartItem.objects.filter(cart=cart, product=product).first()

        if cart_item:
            # El producto ya existe en el carrito, actualizar la cantidad
            cart_item.quantity += quantity
            cart_item.save()
        else:
            # El producto no existe en el carrito, crear un nuevo elemento del carrito
            cart_item = CartItem.objects.create(
                cart=cart, product=product, quantity=quantity)

        return Response({'message': 'Producto agregado al carrito exitosamente'})
    except Product.DoesNotExist:
        return Response({'message': 'El producto no existe'}, status=400)
