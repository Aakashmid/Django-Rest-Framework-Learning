from rest_framework import serializers
from .models import Quizzes,Question,Answer



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quizzes
        fields=['title',]


# class AnswerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Answer
#         fields=['answer_text']

class RandomQuestionSerializer(serializers.ModelSerializer):
    # answer=AnswerSerializer(read_only=True)
    class Meta:
        model = Question
        fields=['title','answer']