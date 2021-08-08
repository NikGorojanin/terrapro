from django.shortcuts import render, redirect, reverse
from django.views import View

from api.models import Post

from post.form import PostForm


class CreateView(View):
    def get(self, request):
        form = PostForm()

        return render(request, template_name='post.html', context={'form': form})

    def post(self, request):
        form = PostForm(request.POST, request.FILES)

        if not form.is_valid():
            return render(request, template_name='post.html', context={'form': form})

        post = Post(
            text_rus=form.cleaned_data.get('text_rus'),
            text_eng=form.cleaned_data.get('text_eng'),
            text_uzb=form.cleaned_data.get('text_uzb'),
            desposition=form.cleaned_data.get('desposition'),
            tg_image_id=form.cleaned_data.get('image'),
            tg_video_id=form.cleaned_data.get('video'),
            tg_document_id=form.cleaned_data.get('document'),
            is_published=form.cleaned_data.get('is_published'),
        )
        post.save()

        return redirect(reverse('post:list'))
