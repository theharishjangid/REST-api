from rest_framework.serializers import ModelSerializer
from qv1.models import Quiz, Questions

class QuizSerializer(ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'