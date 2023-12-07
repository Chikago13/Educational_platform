from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return obj.generate_jwt()

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'token']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class UserCreateWithSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        token = user.generate_jwt()  # генерируем токен для нового пользователя
        return user, token
    

class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'token']
        read_only_fields = ['id', 'is_active', 'is_staff']

    def get_token(self, obj):
        # вызываем метод generate_jwt модели User для генерации токена
        return obj.generate_jwt()


    # def validate_token(self, value):
    #     # проверяем, что токен не пустой и декодируем его, чтобы получить user_id
    #     if not value:
    #         raise serializers.ValidationError("Token is required")
    #     user_id = User.decode_jwt(value)
    #     if isinstance(user_id, str):
    #         raise serializers.ValidationError(user_id)
    #     return value

    # def validate_user(self, value):
    #     # проверяем, что пользователь существует в базе данных
    #     try:
    #         user = User.objects.get(pk=value)
    #     except User.DoesNotExist:
    #         raise serializers.ValidationError("User does not exist")
    #     return user




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        refresh = RefreshToken.for_user(user)

        token["refresh"] = str(refresh)
        token["username"] = user.email

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)["refresh"]
        data["refresh"] = refresh
        data["username"] = self.user.email
        data["jwt"] = self.user.generate_jwt()
        # data['access'] = str(self.get_token(self.user)['access'])
        return data


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(read_only=True)
    token = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        token = attrs.get('token')
        user = User.objects.get(email=email)

        if token:
            decoded_token = User.decode_jwt(token)
            if not isinstance(decoded_token, str):
                return {
                    'email': user.email,
                    'token': token
                }
            else:
                raise serializers.ValidationError(decoded_token)

        if email and password:
            if user and user.check_password(password):
                refresh = RefreshToken.for_user(user)
                return {
                    'email': user.email,
                    'token': str(refresh.access_token)
                }
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'email' and 'password', or 'token'.")
        


        

