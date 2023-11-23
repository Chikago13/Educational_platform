from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    ArticleViewSet,
    CourseArticlesTopicsAPIView,
    CourseViewSet,
    SpecializationViewSet,
    StudentCourseRecommendationView,
    TopicViewSet,
    # CourseStudentView,
)

router = DefaultRouter()
router.register(r"specialization", SpecializationViewSet)
router.register(r"course", CourseViewSet)
router.register(r"article", ArticleViewSet)
router.register(r"topic", TopicViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "course/(?P<pk>[^/.]+)/articles_topic",
        CourseArticlesTopicsAPIView.as_view(),
        name="articles_topic",
    ),
    re_path(
        "student/(?P<pk>[^/.]+)/course",
        StudentCourseRecommendationView.as_view(),
        name="student_course",
    ),
    #     re_path(
    #     "course/(?P<pk>[^/.]+)/student",
    #     CourseStudentView.as_view(),
    #     name="course_student",
    # ),
]
