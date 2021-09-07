from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from login.forms import CreateUserForm


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
            return redirect('log')
        context = {
            'form': form,
        }
        return render(request, 'login/reg.html', context)


def logout_func(request):
    logout(request)
    return redirect('log')
