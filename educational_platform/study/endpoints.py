from rest_framework import viewsets
from itertools import chain

from mentorship.models import Student

from .models import Article, Course, Specialization, Topic
from rest_framework.generics import ListAPIView
from .serializers import (
    ArticleSerializer,
    CourseSerializer,
    SpecializationSerializer,
    TopicSerializer,
    ArticleTopicSerializer,
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
        course = self.kwargs['pk']
        articles = Article.objects.filter(course_id=course)
        topics = Topic.objects.filter(course_id=course)
        queryset = list(chain(articles, topics))
        return queryset
    

# получение рекомендации курсов для определенного студента
class StudentCourseRecommendationView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        student_id = self.kwargs['pk'] 
        student = Student.objects.get(id=student_id)
        student_courses = Course.objects.all()
        student_specializations = Specialization.objects.filter(course__in=student_courses)
        recommended_courses = Course.objects.filter(specialization__in=student_specializations).exclude(id__in=student_courses)
        return recommended_courses
    
