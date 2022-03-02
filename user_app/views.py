from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.views import APIView
from user_app.serializers import RegistrationSerializer, LoginSerializer
from user_app import models


class LogoutView(APIView):
    
    def post(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class RegistrationView(APIView):

    def post(self, request, format=None):
        serializer = RegistrationSerializer(data = request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful!"
            data['username'] = account.username
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)
            
            data['token'] = {
                                'refresh': str(refresh),
                                'access': str(refresh.access_token),
                            }

        else:
            data = serializer.errors

        return Response(data)


class LoginView(APIView):

    def post(self, request, format=None):
        serializer = LoginSerializer(data = request.data)
        data = {}

        # if serializer.is_valid():
            

