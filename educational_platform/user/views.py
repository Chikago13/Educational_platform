from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def obtain_token(request):
    # получаем email и password из запроса
    email = request.data.get('email')
    password = request.data.get('password')

    # проверяем, что email и password были переданы
    if not email or not password:
        return Response(
            {'error': 'Both email and password are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    # ищем пользователя с переданным email в базе данных
    user = User.objects.filter(email=email).first()

    # аутентификация пользователя
    if user and user.check_password(password):
        # если пользователь найден и пароль совпадает, генерируем токен
        refresh = RefreshToken.for_user(user)
        serializer = UserSerializer(user)
        return Response({
            'token': str(refresh.access_token),
            'user': serializer.data
        })
    else:
        return Response(
            {'error': 'Invalid email or password'},
            status=status.HTTP_400_BAD_REQUEST
        )

