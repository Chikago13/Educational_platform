from itertools import chain

from mentorship.models import Group, Student
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Article, Course, Specialization, Topic
from .serializers import (
    ArticleSerializer,
    ArticleTopicSerializer,
    CourseSerializer,
    SpecializationSerializer,
    TopicSerializer,
)


class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


# всех статей и тем определенного курса
class CourseArticlesTopicsAPIView(ListAPIView):
    serializer_class = ArticleTopicSerializer

    def get_queryset(self):
        course = self.kwargs["pk"]
        articles = Article.objects.filter(course_id=course)
        topics = Topic.objects.filter(course_id=course)
        queryset = chain(articles, topics)
        return queryset


# получение рекомендации курсов для определенного студента
class StudentCourseRecommendationView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        student_id = self.kwargs["pk"]
        group = Group.objects.filter(students__in=student_id)
        student_courses = Course.objects.filter(id__in=group.values("course"))
        course_specializations = Course.objects.filter(
            specialization__in=student_courses.values("specialization")
        )
        recommended_courses = course_specializations.exclude(
            id__in=student_courses.values("id")
        )
        return recommended_courses


