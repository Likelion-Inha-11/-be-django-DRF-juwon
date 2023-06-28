from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        # Post 안의 모든 정보를 json으로 변환
        fields = '__all__'

        # 특정 필드만 변환
        # fields = ('title', 'content')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'