from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import (
    AnswerViewSet,
    CourseTestListAPIView,
    QuestionAnswerListAPIView,
    QuestionViewSet,
    TestQuestionListAPIView,
    TestViewSet,
)

router = DefaultRouter()
router.register(r"answer", AnswerViewSet)
router.register(r"question", QuestionViewSet)
router.register(r"test", TestViewSet)


urlpatterns = [
    path("", include(router.urls)),
    re_path(
        "course/(?P<pk>[^/.]+)/tests",
        CourseTestListAPIView.as_view(),
        name="course_tests",
    ),
    re_path(
        "test/(?P<pk>[^/.]+)/questions",
        TestQuestionListAPIView.as_view(),
        name="test_questions",
    ),
    re_path(
        "questions/(?P<pk>[^/.]+)/answers",
        QuestionAnswerListAPIView.as_view(),
        name="question_answers",
    ),
]
