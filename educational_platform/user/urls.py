from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import UserLoginView
from .jwt import ObtainTokenPairView
from .views import UserViewSet

router = DefaultRouter()
router.register(r"user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("api/token/", ObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path('login/', UserLoginView.as_view(), name='user-login'),
]


