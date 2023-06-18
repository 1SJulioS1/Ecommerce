from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from app.serializers import CustomUserSerializer
from app.permissions import *
from app.models import CustomUser


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
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
