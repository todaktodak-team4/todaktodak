from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import MemorialHall, Wreath, Message

class MemorialHallSerializer(ModelSerializer) :
    class Meta :
        model = MemorialHall
        # fields = '__all__'
        fields = ['id', 'name', 'date', 'info', 'public', 'private', 'thumbnail', 'participation', 'token']
        
    extra_kwargs = {
            'participation': {'required': False, 'default': []},
            'token': {'read_only': True}  # token 필드를 읽기 전용으로 설정
        }

class WreathSerializer(ModelSerializer) :
    nickname = serializers.ReadOnlyField(source = 'nickname.nickname')
    profile = serializers.SerializerMethodField()
    
    class Meta :
        model = Wreath
        fields = ['id', 'donation', 'comment', 'name', 'hall', 'nickname', 'profile', 'created_at']
        
    def get_profile(self, obj):
        if obj.nickname.profile and hasattr(obj.nickname.profile, 'url'):
            return obj.nickname.profile.url
        return None  # 기본 이미지 URL을 반환하거나 None을 반환
        
class MessageSeralizer(ModelSerializer) :
    nickname = serializers.ReadOnlyField(source = 'nickname.nickname')
    profile = serializers.SerializerMethodField()
    
    class Meta :
        model = Message
        fields = ['id', 'content', 'hall', 'nickname', 'profile', 'created_at']
        
    def get_profile(self, obj):
        if obj.nickname.profile and hasattr(obj.nickname.profile, 'url'):
            return obj.nickname.profile.url
        return None  # 기본 이미지 URL을 반환하거나 None을 반환