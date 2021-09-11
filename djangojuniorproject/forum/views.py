from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
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
            obj = form.save(commit=False)
            obj.owner = request.user
            obj.save()
            messages.success(request, f'Question was successfully created.')
            return redirect('forum')


class EditPostPage(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)

        if post.owner == request.user:
            form = PostForm(initial={'title': post.title, 'text': post.text})
            return render(request, 'forum/edit.html', context={'form': form, 'post': post})
        return HttpResponseForbidden()

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        form = PostForm(request.POST)
        if post.owner == request.user and form.is_valid():
            post.title = request.POST['title']
            post.text = request.POST['text']
            post.save()
            messages.success(request, f'Question {post_id} was successfully edited.')
            return redirect('forum')
        return HttpResponseForbidden()


class DeleteProjectPage(LoginRequiredMixin, View):
    login_url = '/acc/log/'
    redirect_field_name = 'log'

    def get(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.owner == request.user:
            delete_word = '/'.join(list(map(str, [post.owner, post.pk])))
            return render(request, 'forum/delete.html', context={'post': post, 'word': delete_word})
        return HttpResponseForbidden()

    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        if post.owner == request.user:

            delete_confirm = request.POST.get('confirm')
            delete_word = '/'.join(list(map(str, [post.owner, post.pk])))

            if delete_confirm == delete_word:
                post.delete()
                messages.success(request, f'Question {post_id} was successfully deleted.')
                return redirect('forum')
            messages.error(request, 'Confirm word is incorrect.')
            return render(request, 'forum/delete.html', context={'post': post, 'word': delete_word})
        return HttpResponseForbidden()

