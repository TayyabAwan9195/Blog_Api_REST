from .models import Post,Comment
from rest_framework import serializers
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model=Post
        fields='__all__'


