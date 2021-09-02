from django.urls import path
from .views import ForumMainPage


urlpatterns = [
    path('', ForumMainPage.as_view(), name='forum'),
]
