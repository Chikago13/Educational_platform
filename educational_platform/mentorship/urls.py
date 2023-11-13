from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentTeacherListAPIView

# router = DefaultRouter()
# router.register(r'student_teacher', StudentTeacherListAPIView)

urlpatterns = [
    # path('', include(router.urls)),
    path('student_teacher/', StudentTeacherListAPIView.as_view(), name='student_teacher-list')

]