from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import UserLoginView, CreateUserWithToken, create_user
from .jwt import ObtainTokenPairView
from .views import UserViewSet, obtain_token


router = DefaultRouter()
router.register(r"user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", ObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('token/', obtain_token, name='token'),
    path('create/', create_user, name='create_user'),
    path('create_user/', CreateUserWithToken.as_view(), name='create_user'),
]


