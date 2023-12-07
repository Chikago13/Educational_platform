from .serializers import UserLoginSerializer
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response



class LoginAPIView(APIView):
    serializers_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data.get('user')
        serializer = self.serializers_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
        