from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken

from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        return obj.generate_jwt()


    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'token']
        read_only_fields = ['id', 'is_active', 'is_staff']




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
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        token = attrs.get('token')
        user = User.objects.filter(email=email).first()

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
        


        

