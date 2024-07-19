from rest_framework.serializers import ModelSerializer
from .models import rememberTree, Photo


class RememberSerializer(ModelSerializer):
    class Meta:
        model = rememberTree
        fields = ['id', 'treeName', 'myName', 'flowerType', 'growth_period']


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields =['id', 'rememberPhoto','description','rememberDate','comment','remember_tree']