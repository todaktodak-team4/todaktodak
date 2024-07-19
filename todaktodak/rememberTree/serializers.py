from rest_framework.serializers import ModelSerializer
from .models import rememberTree

class RememberSerializer(ModelSerializer):
    class Meta:
        model = rememberTree
        fields = ['id', 'treeName', 'myName', 'flowerType', 'growth_period']
