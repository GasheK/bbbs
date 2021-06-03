from rest_framework import generics

from bbbs.questions.models import Question
from bbbs.questions.serializers import (
    QuestionGetSerializer,
    QuestionPostSerializer
)


class QuestionsList(generics.ListAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionGetSerializer
        else:
            return QuestionPostSerializer


class QuestionView(generics.RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionPostSerializer
