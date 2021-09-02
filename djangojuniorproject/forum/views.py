from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ForumMainPage(View):
    def get(self, request):
        return render(request, 'forum/index.html', {})
