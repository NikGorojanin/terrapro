from django.shortcuts import render
from django.views import View

from post.form import PostForm


class PostView(View):
    def get(self, request):
        form = PostForm()

        return render(request, template_name='post.html', context={'form': form})

    def post(self, request):
        pass
