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
        return super().patch(request, *args, **kwargs)

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
        operation_description="Delete a single instance of Category",
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


class CartView(APIView):
    """
        Cart related view
    """
    permission_classes = [IsBuyer]

    @swagger_auto_schema(
        operation_description="Add items to cart",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'cart_items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'product': openapi.Schema(type=openapi.TYPE_STRING),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
                        },
                        required=['product', 'quantity']
                    )
                ),
            },
            required=['cart_items']
        ),
        responses={
            201: "Cart created successfully",
            400: "Bad request: Insufficient product quantity",
            401: "Unauthorized",
            404: "Not found: Product not found or no cart_items provided"
        },
        manual_parameters=token_as_parameters
    )
    def post(self, request):
        user = request.user

        # Crear un nuevo carrito para el usuario si no existe
        cart, created = Cart.objects.get_or_create(user=user)

        # Obtener los datos de los cart_items del request
        cart_items_data = request.data.get('cart_items')

        # Verificar si se enviaron datos de cart_items
        if not cart_items_data:
            return Response({'error': 'No cart_items provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Añadir o actualizar cada cart_item en el carrito
        for cart_item_data in cart_items_data:
            product_id = cart_item_data.get('product')
            quantity = cart_item_data.get('quantity')

            # Verificar si se enviaron los datos necesarios
            if not product_id or not quantity:
                return Response({'error': 'Invalid cart_item data'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                product = Product.objects.get(name=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            if quantity > product.quantity:
                return Response({'error': 'Insufficient product quantity'}, status=status.HTTP_400_BAD_REQUEST)

            # Verificar si el producto ya existe en el carrito
            cart_item = cart.cartitem_set.filter(product=product).first()

            if cart_item:
                # Si el producto ya existe, actualizar la cantidad en el cart_item y disminuir la existencia del producto
                cart_item.quantity += quantity
                cart_item.save()
            else:
                # Si el producto no existe, crear un nuevo cart_item y añadirlo al carrito
                CartItem.objects.create(
                    cart=cart, product=product, quantity=quantity)

            # Disminuir la existencia del producto
            product.quantity -= quantity
            product.save()

        return Response({'message': 'Cart updated successfully'}, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="Retrieve cart items for logged user",
        responses={
            200: CartItemSerializer(many=True),
            401: "Unauthorized",
        }
    )
    def get(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(cart__user_id=user)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="Delete all cart items for a user",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Success message"
                        )
                    }
                )
            ),
            400: openapi.Response(
                description="Bad request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    }
                )
            ),
            401: openapi.Response(
                description="Unauthorized",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'detail': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description="Error message"
                        )
                    }
                )
            )
        }
    )
    def delete(self, request):
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items.delete()
            return Response({'message': "success"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({'error': "user doesn't have associated cart "}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description='Update quantity of cart item',
        responses={
            200: openapi.Response(description='Cart item updated successfully'),
            400: openapi.Response(description="Bad Request", examples={
                "application/json": {
                    "error": "Error message"
                }
            }),
            404: openapi.Response(description="Not Found", examples={
                "application/json": {
                    "error": "Error message"
                }
            }),
            401: openapi.Response(description="Unauthorized", examples={
                "application/json": {
                    "error": "Unauthorized"
                }
            })
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'cart_items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'product': openapi.Schema(type=openapi.TYPE_STRING),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER)
                        }
                    )
                )
            },
            required=['cart_items']
        )
    )
    def patch(self, request):
        """
            Update quantity of cart item
        """
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            return Response({'error': "user doesn't have associated cart "}, status=status.HTTP_400_BAD_REQUEST)

        try:
            cart_item = CartItem.objects.get(cart=cart)
        except CartItem.DoesNotExist:
            return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_items_data = request.data.get('cart_items')
        if not cart_items_data:
            return Response({'error': 'No cart_items provided'}, status=status.HTTP_400_BAD_REQUEST)

        for cart_item_data in cart_items_data:
            product_name = cart_item_data.get('product')
            quantity = cart_item_data.get('quantity')

            if not product_name or not quantity:
                return Response({'error': 'Invalid cart_item data'}, status=status.HTTP_400_BAD_REQUEST)

            if cart_item.product.name == product_name:
                # if quantity is added
                product = Product.objects.get(name=product_name)
                if quantity > cart_item.quantity:
                    if quantity > product.quantity:
                        return Response({'error': 'Insufficient product quantity'}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        product.quantity -= quantity - cart_item.quantity
                        product.save()
                else:
                    product.quantity += cart_item.quantity - quantity
                    product.save()
                cart_item.quantity = quantity
                cart_item.save()

                return Response({'message': 'Cart item updated successfully'})

        return Response({'error': 'Cart item not found in the request'}, status=status.HTTP_404_NOT_FOUND)


class CourierListCreateView(generics.ListCreateAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsAdmin]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'availability']
    ordering_fields = ['name', 'availability', 'phone']
    lookup_field = 'name'


class CourierDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer
    permission_classes = [IsAdmin]

    @swagger_auto_schema(
        operation_description="Retrieve a single instance of Courier",
        responses={
            200: CourierSerializer(),
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Courier",
        responses={
            200: CourierSerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a single instance of Courier",
        responses={
            200: CourierSerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a single instance of Courier",
        responses={
            204: "Remove success",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class OrderView(APIView):
    """
        Order related view
    """
    permission_classes = [IsBuyer]

    @swagger_auto_schema(
        operation_summary="Create an order",
        operation_description="Create an order with cart items and address",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'cart_items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'product': openapi.Schema(type=openapi.TYPE_STRING),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER),
                        }
                    )
                ),
                'address': openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'number': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'street': openapi.Schema(type=openapi.TYPE_STRING),
                        'city': openapi.Schema(type=openapi.TYPE_STRING),
                        'state': openapi.Schema(type=openapi.TYPE_STRING),
                        'extra_info': openapi.Schema(type=openapi.TYPE_STRING, nullable=True),
                    }
                ),
            },
            required=['cart_items', 'address'],
        ),
        responses={
            201: "Order created",
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
    )
    def post(self, request):

        cart_itemms_data = request.data.get('cart_items')
        address_data = request.data.get('address')

        if not cart_itemms_data:
            return Response({'error': 'No cart_items provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not address_data:
            return Response({'error': 'No address provided'}, status=status.HTTP_400_BAD_REQUEST)

        address = Address.objects.create(number=address_data.get('number'), street=address_data.get('street'),
                                         city=address_data.get('city'), state=address_data.get('state'), extra_info=address_data.get('extra_info'))
        address.save()
        courier = Courier.objects.filter(availability=True).first()

        order = Order.objects.create(
            user=request.user, address=address, courier=courier)

        for cart_item_data in cart_itemms_data:
            product = cart_item_data.get('product')
            quantity = cart_item_data.get('quantity')

            if not product or not quantity:
                return Response({'error': 'Invalid cart_item data'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                product = Product.objects.get(name=product)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            OrderItem.objects.create(
                order=order, product=product, quantity=quantity
            )
        try:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            cart_items.delete()
            return Response({'message': "Order created"}, status=status.HTTP_201_CREATED)
        except Cart.DoesNotExist:
            return Response({'error': "user doesn't have associated cart "}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Retrieve cart items for logged user",
        responses={
            200: OrderItemSerializer(many=True),
            401: "Unauthorized",
        }
    )
    def get(self, request):
        order_items = OrderItem.objects.filter(
            order__status='processing', order__user=request.user)
        serializer = OrderItemSerializer(order_items, many=True)
        return Response(serializer.data)


class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsBuyer]

    @swagger_auto_schema(
        operation_description="Update a single instance of Order",
        responses={
            200: OrderSerializer(),
            400: "Bad request",
            401: "Unauthorized",
            404: "Not found"
        },
        manual_parameters=token_as_parameters

    )
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
