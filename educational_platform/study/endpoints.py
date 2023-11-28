from itertools import chain

from mentorship.models import Group, Student
from mentorship.serializers import GroupSerializer, StudentSerializer
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


# получения всех курсов для определенного студента
class CourseStudentView(ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        students = self.kwargs["pk"]
        group = Group.objects.filter(students__id=students)
        course = Course.objects.filter(group__in=group)
        return course


# рекомендации курсов студенту на основании курсов, которые посещают его одногруппники
class StudentCourseGroupmatesRecommendationView(ListAPIView):
    serializer_class = CourseSerializer

    # def get_queryset(self):
    #     student_id = self.kwargs["pk"]
    #     student_groups = Group.objects.filter(id = student_id) #  Получаем все группы , где содержится студент
    #     group_students = Student.objects.filter(group__in = student_groups).exclude(id = student_id) # Получаем все одногрупников нашего студента
    #     recommended_courses = Course.objects.filter(students__in=group_students)  # Фильтруем курсы, которые посещают одногруппники данного студента
    #     return recommended_courses

    def get_queryset(self):
        student_id = self.kwargs["pk"]
        groups = Group.objects.filter(
            students__id=student_id
        )  # We find all the groups in which this student studies
        student_courses = Course.objects.filter(
            group__in=groups
        )  # We find courses related to these groups
        recommended_courses = Course.objects.exclude(
            group__students=student_id
        )  # We find recommended courses, excluding courses related to the student
        return recommended_courses
