from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    GroupViewSet,
    StudensCourseAPIView,
    StudentGroupAPIView,
    StudentTeacherListAPIView,
    StudentViewSet,
    TeacherSpecializationAPIView,
    TeacherViewSet,
)

router = DefaultRouter()
router.register(r"teacher", TeacherViewSet)
router.register(r"student", StudentViewSet)
router.register(r"group", GroupViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "student_teacher/",
        StudentTeacherListAPIView.as_view(),
        name="student_teacher-list",
    ),
    re_path(
        "group/(?P<pk>[^/.]+)/students",
        StudentGroupAPIView.as_view(),
        name="student_group",
    ),
    re_path(
        "specialization/(?P<pk>[^/.]+)/teacher",
        TeacherSpecializationAPIView.as_view(),
        name="specialization_teacher",
    ),
    re_path(
        "course/(?P<pk>[^/.]+)/students",
        StudensCourseAPIView.as_view(),
        name="course_student",
    ),
]
