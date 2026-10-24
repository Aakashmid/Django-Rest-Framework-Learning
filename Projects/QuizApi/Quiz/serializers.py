from rest_framework import serializers
from .models import Quizzes,Question,Answer



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quizzes
        fields=['title',]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields=['id','answer_text','is_right']

class RandomQuestionSerializer(serializers.ModelSerializer):
    # answer is related name b/w  relation of Question and Answer model
    answer=AnswerSerializer(many=True, read_only=True)  # give fields which is included in AnswerSerializers fields
    class Meta:
        model = Question
        fields=['title','answer']