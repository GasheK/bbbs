from rest_framework import generics

from bbbs.questions.models import Question
from bbbs.questions.serializers import (
    QuestionGetSerializer,
    QuestionPostSerializer
)


class QuestiosList(generics.ListCreateAPIView):
    queryset = Question.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return QuestionGetSerializer
        else:
            return QuestionPostSerializer
