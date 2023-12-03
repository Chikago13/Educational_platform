from constant.mixin import DateTimeMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import jwt
from datetime import datetime, timedelta
from django.conf import settings

from .manager import UserManager


class User(DateTimeMixin, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def generate_jwt(self):
        payload = {
            'user_id': self.pk,
            'exp': datetime.utcnow() + timedelta(days=1),
            'iat': datetime.utcnow()
        }
        return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    
    @staticmethod
    def decode(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return payload["user_id"]
        except jwt.ExpiredSignatureError:
            return "Token expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
        

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return f"{self.first_name}"

    def __str__(self):
        return f"{self.email}"
