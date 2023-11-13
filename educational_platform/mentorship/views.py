from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from itertools import chain

from .models import Teacher, Student, Group
from .serializers import TeacherSerializer, StudentSerializer, GroupSerializer, TeacherStudentSerializer

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
    student = Student.objects.all()
    teacher =Teacher.objects.all()
    queryset = chain(student, teacher)
    serializer_class = TeacherStudentSerializer