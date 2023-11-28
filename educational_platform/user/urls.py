from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet
from .jwt import ObtainTokenPairView

router = DefaultRouter()
router.register(r"user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('api/token/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
]
