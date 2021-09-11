from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


from login.forms import CreateUserForm, EditUserProfileForm
from login.models import UserProfile

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('forum')
        return render(request, 'login/log.html', {})

    def post(self, request):
        if not request.user.is_authenticated:
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('forum')
            messages.info(request, 'Incorrect login or password. Try again')
            return render(request, 'login/log.html', {})


class RegistrationPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('forum')
        form = CreateUserForm()
        context = {
            'form': form,
        }
        return render(request, 'login/reg.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('forum')
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = User.objects.get(username=request.POST['username'])

            user_profile = UserProfile(user_id=user.id)
            user_profile.save()
            return redirect('log')
        context = {
            'form': form,
        }
        return render(request, 'login/reg.html', context)


def logout_func(request):
    logout(request)
    return redirect('log')


class ProfileView(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request):
        user_profile = EditAboutProfileView.profile_object(request.user.id)
        return render(request, 'login/profile.html', context={'profile': user_profile})


class EditAboutProfileView(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request):
        user_profile = EditAboutProfileView.profile_object(request.user.id)

        initial_data = {
            'avatar': user_profile.avatar,
            'email': user_profile.user.email,
            'about': user_profile.about,
        }
        form = EditUserProfileForm(initial=initial_data)
        return render(request, 'login/edit-profile.html', context={'profile': user_profile, 'form': form})

    def post(self, request):
        form = EditUserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            user.email = request.POST['email']
            user.save()
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('edit')
        return render(request, 'log/edit-profile.html', context={'form': form})

    @staticmethod
    def profile_object(user_id):
        try:
            prof = UserProfile.objects.get(user_id=user_id)
        except ObjectDoesNotExist:
            prof = UserProfile(user_id=user_id)
            prof.save()
        return prof


class UserProfileView(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request, username):
        if username == request.user.username:
            return redirect('profile')

        user_profile = get_object_or_404(UserProfile, user__username=username)

        return render(request, 'login/profile.html', context={'profile': user_profile})


class SubscribeView(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request, username):
        user_profile = UserProfile.objects.get(user__username=username)
        if username != request.user.username and request.user not in user_profile.subscribers.all():
            user_profile.subscribers.add(request.user)

        return redirect('user-profile', username=username)


class UnsubscribeView(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request, username):
        user_profile = UserProfile.objects.get(user__username=username)
        if username != request.user.username and request.user in user_profile.subscribers.all():
            user_profile.subscribers.remove(request.user)

        return redirect('user-profile', username=username)


