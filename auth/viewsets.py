import jwt
from django.contrib.auth import authenticate
from decouple import config
from datetime import datetime, timedelta
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth.serializers import UserSerializer


class TokenHanlder:

    def generate_jwt_token(self, user):
        payload = {
            'user_id': user.id,
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(days=1),
        }
        return jwt.encode(
            payload,
            config('SECRET_KEY'),
            algorithm='HS256'
        )


class LoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'Please provide both username and password'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token = TokenHanlder().generate_jwt_token(user)
        serializer = UserSerializer(user)

        return Response({
            'user': serializer.data,
            'token': token
        })
