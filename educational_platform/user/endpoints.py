from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


    

class UserLoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)  # Проверяем валидность данных

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        token = serializer.validated_data.get("token")

        # Проведем аутентификацию на основе email и password
        user = authenticate(email=email, password=password)

        if user:
            # Если аутентификация прошла успешно, генерируем токен
            refresh = RefreshToken.for_user(user)

            # Возвращаем email и токен
            return Response({
                'email': email,
                'token': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            })
        else:
            return Response({'error': 'Неправильный email или пароль'}, status=status.HTTP_401_UNAUTHORIZED)