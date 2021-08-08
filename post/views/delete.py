from django.shortcuts import redirect, reverse
from django.views import View

from api.models import Post


class DeleteView(View):
    def post(self, request, post_id):
        Post.objects.get(pk=post_id).delete()

        return redirect(reverse('post:list'))
