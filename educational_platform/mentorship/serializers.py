from rest_framework import serializers, viewsets

from .models import Group, Student, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    def get_age(self, obj):
        return obj.get_age()

    class Meta:
        model = Student
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class TeacherStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        field = "__all__"

    # def to_representation(self, instance):
    #     if isinstance(instance, Teacher):
    #         serializer = TeacherSerializer(instance)
    #     elif isinstance(instance, Student):
    #         serializer = StudentSerializer(instance)
    #     else:
    #         raise ValueError()
    #     return serializer.data

    def to_representation(self, instance):
        match instance:
            case Teacher():
                serializer = TeacherSerializer(instance)
            case Student():
                serializer = StudentSerializer(instance)
            case _:
                raise ValueError()
        return serializer.data
