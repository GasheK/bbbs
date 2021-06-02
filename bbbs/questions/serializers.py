from rest_framework import serializers

from bbbs.questions.models import Question


class QuestionGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = serializers.ALL_FIELDS


class QuestionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question')
