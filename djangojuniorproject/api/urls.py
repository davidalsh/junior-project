from django.urls import path
from .views import PostsListView, PostCreateDetailView, PostDetailView


urlpatterns = [
    path('all/', PostsListView.as_view()),
    path('post/create/', PostCreateDetailView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
]
