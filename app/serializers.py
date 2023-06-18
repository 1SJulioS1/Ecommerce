from rest_framework import serializers
from app.models import CustomUser, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email',
                  'password', 'user_type', 'address']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        user = CustomUser.objects.create(**validated_data)

        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address = address_serializer.save()

        user.address = address
        user.set_password(validated_data['password'])
        user.save()

        return user
