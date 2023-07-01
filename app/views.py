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
                operation_description='Retrieve user profile data'
            ),
        },
        manual_parameters=token_as_parameters
    )
    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description="Success",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'data': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            description="Response data"
                        )
                    },
                    required=['data']
                )
            ),
            400: openapi.Response(
                description="Bad Request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    },
                    required=['error']
                )
            ),
        },
        manual_parameters=token_as_parameters
    )
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

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    """
    Logout from the system
    """
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='Success',
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING),
                    },
                ),
                operation_description='Retrieve user profile data'
            ),
        },
        manual_parameters=token_as_parameters
    )
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout succeeded"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    """
    View all user data
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = ['usernname']

    @swagger_auto_schema(
        responses={
            200: CustomUserSerializer(many=True),
            400: openapi.Response(
                description="Unauthorized",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    },
                    required=['error']
                ),
                operation_description='Not allowed to enter this view'

            ),
        },
        manual_parameters=token_as_parameters

    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']

    @swagger_auto_schema(
        responses={
            200: CategorySerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        responses={
            200: CategorySerializer(many=True),
            400: openapi.Response(
                description="Unauthorized",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    },
                    required=['error']
                ),
                operation_description='Not allowed to enter this view'

            ),
        },
        manual_parameters=token_as_parameters
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CategoryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
    lookup_field = 'slug'

    @swagger_auto_schema(
        operation_description="Retrieve, update, or delete a single instance of Category",
        responses={
            200: CategorySerializer(),
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Category",
        responses={
            200: CategorySerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Category",
        responses={
            200: CategorySerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a single instance of MyModel",
        responses={
            204: "Remove success",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        responses={
            200: ProductSerializer(many=True),
            401: openapi.Response(
                description="Unauthorized",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    },
                    required=['error']
                ),
                operation_description='Not allowed to enter this view'

            ),
            400: "Bad request",
        },
        manual_parameters=token_as_parameters
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProductDetailView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    ordering_fields = ['name', 'category', 'price']
    lookup_field = 'slug'

    @swagger_auto_schema(
        responses={
            200: ProductSerializer(many=True),
        },
        operation_description="Retrieve a single instance of Product",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdmin]
    lookup_field = 'slug'

    @swagger_auto_schema(
        operation_description="Retrieve a single instance of Product",
        responses={
            200: ProductSerializer(),
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Product",
        responses={
            200: ProductSerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Product",
        responses={
            200: ProductSerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a single instance of Product",
        responses={
            204: "Remove success",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category', 'price']
    ordering_fields = ['name', 'category', 'price']
    lookup_field = 'slug'

    @swagger_auto_schema(
        responses={
            200: ProductSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


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
