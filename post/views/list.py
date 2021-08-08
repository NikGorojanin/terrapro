from django.shortcuts import render
from django.views import View

from api.models import Post


class PostList(View):
    def get(self, request):
        posts = Post.objects.all()

        return render(request, template_name='posts.html', context={'posts': posts})
