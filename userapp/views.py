from .serializers import RegisterUserSerializer
from .models import NewUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# Create your views here.

class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        # Perform authentication
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            response_data = {
                'access': str(access_token),
                'refresh': str(refresh_token),
                'user_name': user.user_name
            }

            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        reg_serializer = RegisterUserSerializer(data = request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



