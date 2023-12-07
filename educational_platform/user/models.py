from constant.mixin import DateTimeMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
import jwt
from educational_platform.settings import SECRET_KEY

from .manager import UserManager
from datetime import datetime, timedelta


class User(DateTimeMixin, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return f"{self.first_name}"

    def __str__(self):
        return f"{self.email}"
    
    def _generet_jwt_token(self):
        dt = datetime.now() + timedelta(days = 1)
        token = jwt.encode({'id': self.pk, 
                            'email': self.email, 
                            'exp': int(dt.strftime('%s'))}, 
                            SECRET_KEY, 
                            algorithm = 'HS256')
        return token

    @property
    def token(self):
        return self._generet_jwt_token()
    
