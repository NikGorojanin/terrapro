import os
from django.forms import forms


def validate_image(image):
    ext = os.path.splitext(image.name)[1]
    valid_extensions = ['.jpg', '.png', '.jpeg']

    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Не поддерживаемый тип изображения')


def validate_video(video):
    ext = os.path.splitext(video.name)[1]
    valid_extensions = ['.mp4']

    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Не поддерживаемый тип видео')


def validate_document(document):
    ext = os.path.splitext(document.name)[1]
    valid_extensions = ['.doc', '.docx']

    if not ext.lower() in valid_extensions:
        raise forms.ValidationError('Не поддерживаемый тип документа')
