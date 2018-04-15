from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ReadOnlyModelViewSet

from Post.models import Post
from Post.serializers import PostSerializer


class PostViewSet(ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)