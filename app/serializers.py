from .models import CustomUser
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

import requests
from datetime import timedelta
from django.core.files.temp import NamedTemporaryFile

from app.models import CustomUser, Address, Category, Product


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'user_type', 'phone', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'image']
        depth = 1

    def get_image(self, obj):
        if obj.image.url.startswith('http'):  # Verifica si es una URL
            return obj.image.url
        else:
            return obj.image.name

    def validate_image(self, value):
        if value.startswith('http'):  # Verifica si es una URL
            try:
                response = requests.get(value, timeout=10)
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(response.content)
                img_temp.flush()
                return img_temp
            except requests.exceptions.RequestException:
                raise serializers.ValidationError(
                    'Error al descargar la imagen desde la URL.')
        else:
            return value
