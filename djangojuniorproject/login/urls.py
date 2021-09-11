from django.urls import path
from .views import LoginPage, RegistrationPage, logout_func, ProfileView, UserProfileView, EditAboutProfileView, \
    SubscribeView, UnsubscribeView

urlpatterns = [
    path('log/', LoginPage.as_view(), name='log'),
    path('reg/', RegistrationPage.as_view(), name='reg'),
    path('logout/', logout_func, name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
    path('edit/', EditAboutProfileView.as_view(), name='edit'),
    path('subscribe/<str:username>/', SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/<str:username>/', UnsubscribeView.as_view(), name='unsubscribe'),
]
