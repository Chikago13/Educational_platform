import jwt 
from .models import User
from rest_framework import authentication, exceptions as api_exceptions
from educational_platform.settings import SECRET_KEY
from jwt import exceptions as jwt_exceptions


class JWTAuthentication(authentication.TokenAuthentication):

    def authentication(self, request):
        auth_header = authentication.get_authorization_header(request= request).split()
        auth_header_prefix = 'token'

        if not auth_header:
            return None
        if len(auth_header) == 1:
            return None
        if len(auth_header) > 2:
            return None
        
        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if auth_header_prefix != prefix.lower():
            return None
        
        return self._authentication_credentials(token)
    

    @staticmethod
    def _authentication_credentials(token):
        try:
            try:
                payload = jwt.decode(token, SECRET_KEY)
            except jwt_exceptions.DecodeError:
                msg = 'Not valid token'
                raise api_exceptions.AuthenticationFailed(msg)
            try:
                user = User.objects.get(pk = payload['id'])
            except User.DoesNotExist:
                msg = 'User not exist'
                raise api_exceptions.AuthenticationFailed(msg)
            if not user.is_active:
                msg = 'User is not active'
                raise api_exceptions.AuthenticationFailed(msg)
        except Exception:
            msg = 'Server error'
            raise api_exceptions.AuthenticationFailed(msg)
        return user




        

