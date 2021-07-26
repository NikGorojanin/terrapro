from django import forms


class PostForm(forms.Form):
    is_published = forms.BooleanField(label='Опубликовать', initial=True)
    text_rus = forms.TextInput()
    text_eng = forms.TextInput()
    text_uzb = forms.TextInput()
    file = forms.FileField()
