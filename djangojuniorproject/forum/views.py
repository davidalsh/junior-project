from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from forum.models import Post

from forum.forms import PostForm


class ForumMainPage(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request):
        posts = Post.objects.all()

        paginator = Paginator(posts, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        form = PostForm()

        context = {
            'page_obj': page_obj,
            'form': form,
        }

        return render(request, 'forum/index.html', context)

    def post(self, request):
        form = PostForm(request.POST)

        if form.is_valid():
            obj = form.save()
            obj.save()
            return redirect('')


