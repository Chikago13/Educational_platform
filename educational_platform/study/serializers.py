from rest_framework import serializers

from .models import Article, Course, Specialization, Topic


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class ArticleTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        field = "__all__"

    def to_representation(self, instance):
        match instance:
            case Article():
                serializer = ArticleSerializer(instance)
            case Topic():
                serializer = TopicSerializer(instance)
            case _:
                raise ValueError()
        return serializer.data
