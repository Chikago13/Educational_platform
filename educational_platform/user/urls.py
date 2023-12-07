from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .endpoints import LoginAPIView
from .views import UserViewSet


router = DefaultRouter()
router.register(r"user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path('login/', LoginAPIView.as_view(), name='login'),
]
