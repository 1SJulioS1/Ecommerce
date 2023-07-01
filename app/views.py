from .models import Cart, CartItem
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import api_view, permission_classes

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import get_object_or_404


from app.serializers import *
from app.permissions import *
from app.models import *
from .custom_strings import *


class UserRegistrationView(APIView):
    """
    Allows buyers to register in the system
    """
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'email', 'phone', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Phone number field',
                    pattern=r'^[+535]\d{10}$'
                )
            },
        )
    )
    def post(self, request):
        data = request.data.copy()
        data['user_type'] = 'regular_user'
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messsage': 'Completed'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class AdminRegistrationView(APIView):
    """
    Allows Admin to register in the system
    """
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['username', 'email', 'phone', 'password'],
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'phone': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='Phone number field',
                    pattern=r'^[+535]\d{10}$'
                )
            },
        ),
        manual_parameters=token_as_parameters
    )
    def post(self, request):
        data = request.data.copy()
        data['user_type'] = 'admin'
        serializer = CustomUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'messsage': 'Completed'}, status=201)
        return Response(serializer.errors, status=400)


class UserDetailView(APIView):
    """
    Allows users to see and edit its profile info
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='Success',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'email': openapi.Schema(type=openapi.TYPE_STRING),
                        'user_type': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            enum=['regular_user', 'admin']

                        ),
                        'phone': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Phone number field',
                            pattern=r'^[+535]\d{10}$'
                        )
                    },
                ),
            ),
            # Otros códigos de respuesta aquí...
        },
        manual_parameters=token_as_parameters
    )
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        user = CustomUser.objects.get(username=request.user.username)
        allowed_fields = ['email', 'phone', 'username', 'password']
        data = {field: request.data.get(
            field) for field in allowed_fields if field in request.data}
        serializer = CustomUserSerializer(
            user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'password' in data:
                user.set_password(data['password'])
            serializer.save()
            return Response({'message': 'Succeed!'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=400)


class UserLogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout succeeded"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['usernname']


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class CategoryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
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
