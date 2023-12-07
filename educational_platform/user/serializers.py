from rest_framework import serializers

from .models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ["id", "is_active", "is_staff"]


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128, write_only=True)
    token = serializers.CharField(max_length = 255, read_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(username = email, password = password)

        if not all(email or password or user):
            raise serializers.ValidationError('Wrong email or password')
        if not isinstance(user, User):
            raise serializers.ValidationError('Given object is not User instance')
        if not user.is_active: 
            raise serializers.ValidationError('User is not active')
        return {
            'email': user.email,
            'token': user.token
        }


         
