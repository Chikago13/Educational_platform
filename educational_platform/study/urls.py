from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import SpecializationViewSet, CourseViewSet, ArticleViewSet,  TopicViewSet, CourseArticlesTopicsAPIView, StudentCourseRecommendationView

router = DefaultRouter()
router.register(r'specialization', SpecializationViewSet)
router.register(r'course', CourseViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'topic', TopicViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path("articles/(?P<pk>[^/.]+)/topic", CourseArticlesTopicsAPIView.as_view(), name="articles_topic"),
    re_path("student/(?P<pk>[^/.]+)/course", StudentCourseRecommendationView.as_view(), name="student_course"),
]
