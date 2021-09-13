from forum.models import Post

from api.serializers import PostsListSerializer, PostDetailSerializer

from rest_framework import generics
from api.permissions import IsOwnerOrReadOnly


class PostsListView(generics.ListAPIView):  # READ
    serializer_class = PostsListSerializer
    queryset = Post.objects.all()


class PostCreateDetailView(generics.CreateAPIView):  # CREATE
    serializer_class = PostDetailSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):  # READ, UPDATE, DELETE
    serializer_class = PostDetailSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

