from django.shortcuts import render, redirect, reverse
from django.views import View

from api.models import Post

from post.form import PostForm


class EditView(View):
    def get(self, request, post_id):
        post = self._get_post(post_id)

        form = PostForm(post.to_dict())

        return render(request, template_name='post.html', context={'form': form})

    def post(self, request, post_id):
        post = self._get_post(post_id)
        form = PostForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, template_name='post.html', context={'form': form})

        post.text_rus = form.cleaned_data.get('text_rus')
        post.text_eng = form.cleaned_data.get('text_eng')
        post.text_uzb = form.cleaned_data.get('text_uzb')
        post.desposition = form.cleaned_data.get('desposition')
        post.is_published = form.cleaned_data.get('is_published')

        image = form.cleaned_data.get('image')
        print(image)
        if image:
            post.tg_image_id = image

        video = form.cleaned_data.get('video')
        print(video)
        if video:
            post.tg_video_id = video

        document = form.cleaned_data.get('document')
        print(document)
        if document:
            post.tg_document_id = document

        post.save()

        return redirect(reverse('post:list'))

    def _get_post(self, post_id):
        return Post.objects.get(pk=post_id)