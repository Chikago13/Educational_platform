from rest_framework import serializers, viewsets
from .models import Teacher, Student, Group

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        return obj.get_age()

    class Meta:
        model = Student
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class TeacherStudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        field  = '__all__'

    def to_representation(self, instance):
        if isinstance(instance, Teacher):
            serializer = TeacherSerializer(instance)
        elif isinstance(instance, Student):
            serializer =StudentSerializer(instance)
        else:
            raise ValueError()
        return serializer.data


