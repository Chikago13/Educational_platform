from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Answer, Question, Test
from .serializers import AnswerSerializer, QuestionSerializer, TestSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


# получение тестов определенного курса 
class CourseTestListAPIView(ListAPIView):
    serializer_class = TestSerializer 

    def get_queryset(self):
        create_by = self.kwargs['pk']
        queryset = Test.objects.filter(create_by__in = create_by)
        return queryset


# получение вопросов теста  
class TestQuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        test = self.kwargs['pk'] 
        queryset = Question.objects.filter(test_id=test)
        return queryset
    

# получение ответов вопроса
class QuestionAnswerListAPIView(ListAPIView):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question = self.kwargs['pk']
        queryset = Answer.objects.filter(question_id=question)
        return queryset