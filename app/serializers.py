from rest_framework import serializers
from app.models import CustomUser, Address, Category, Product


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'address', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        user.address = address
        user.save()

        return user

    def update(self, instance, validated_data):
        address_data = validated_data.pop('address')
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        address_serializer = AddressSerializer(
            instance.address, data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        instance.address = address
        instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'image']
        depth = 1
