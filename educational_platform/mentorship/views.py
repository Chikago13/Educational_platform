from itertools import chain

from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Group, Student, Teacher
from .serializers import (
    GroupSerializer,
    StudentSerializer,
    TeacherSerializer,
    TeacherStudentSerializer,
)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentTeacherListAPIView(ListAPIView):
    serializer_class = TeacherStudentSerializer

    def get_queryset(self):
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        queryset = list(chain(students, teachers))
        return queryset
