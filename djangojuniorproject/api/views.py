from forum.models import Post

from api.serializers import PostsListSerializer, PostDetailSerializer

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from api.permissions import IsOwnerIsAdminOrReadOnly


class PostsListView(generics.ListAPIView):  # READ
    serializer_class = PostsListSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticated,)


class PostCreateDetailView(generics.CreateAPIView):  # CREATE
    serializer_class = PostDetailSerializer
    permission_classes = (IsAuthenticated,)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):  # READ, UPDATE, DELETE
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerIsAdminOrReadOnly,)

