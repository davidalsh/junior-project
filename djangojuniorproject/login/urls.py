from django.urls import path
from .views import LoginPage, RegistrationPage, logout_func


urlpatterns = [
    path('log/', LoginPage.as_view(), name='log'),
    path('reg/', RegistrationPage.as_view(), name='reg'),
    path('logout/', logout_func, name='logout'),
]
