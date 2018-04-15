from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from Post.models import Post


class PostSerializer(ModelSerializer):
    author = serializers.ReadOnlyField(source='author.id')
    created_at = serializers.ReadOnlyField(source='created_at')
    updated_at = serializers.ReadOnlyField(source='updated_at')
    is_deleted = serializers.ReadOnlyField(source='id_deleted')

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_at', 'updated_at', 'is_deleted')
