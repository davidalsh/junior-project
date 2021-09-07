from django.urls import path
from .views import ForumMainPage, EditPostPage, DeleteProjectPage


urlpatterns = [
    path('', ForumMainPage.as_view(), name='forum'),
    path('edit/<int:post_id>', EditPostPage.as_view(), name='edit-post'),
    path('delete/<int:post_id>', DeleteProjectPage.as_view(), name='delete-post'),
]
