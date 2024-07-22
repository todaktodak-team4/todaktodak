from rest_framework.serializers import ModelSerializer
from .models import rememberTree, Photo, Question, UserQuestionAnswer


class RememberSerializer(ModelSerializer):
    class Meta:
        model = rememberTree
        fields = ['id', 'treeName', 'myName', 'flowerType', 'growth_period']
       

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields =['id', 'rememberPhoto','description','rememberDate','comment','remember_tree']


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = UserQuestionAnswer
        fields = '__all__'