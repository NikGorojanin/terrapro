import os

from django import forms

from post.validators import validate_image, validate_video, validate_document
from post.utils import TelegramCacheManager


class PostForm(forms.Form):
    is_published = forms.BooleanField(label='Опубликовать', initial=True, required=False)
    text_rus = forms.CharField(label='Текст на русском', widget=forms.Textarea)
    text_eng = forms.CharField(label='Текст на английском', widget=forms.Textarea, required=False)
    text_uzb = forms.CharField(label='Текст на узбекском', widget=forms.Textarea, required=False)
    desposition = forms.IntegerField(label='Позиция', initial=0)
    image = forms.FileField(label='Изображение', validators=[validate_image], required=False)
    video = forms.FileField(label='Видео', validators=[validate_video], required=False)
    document = forms.FileField(label='Документ', validators=[validate_document], required=False)

    def clean_image(self):
        return TelegramCacheManager().image_cache(image=self.cleaned_data['image'])

    def clean_video(self):
        return TelegramCacheManager().video_cache(video=self.cleaned_data['video'])

    def clean_document(self):
        return TelegramCacheManager().document_cache(document=self.cleaned_data['document'])

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        pass
