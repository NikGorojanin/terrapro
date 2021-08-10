from django import forms

from api.models import Branche


class BranchForm(forms.ModelForm):
    address_rus = forms.CharField(label='Адрес на русском', widget=forms.Textarea)
    address_uzb = forms.CharField(label='Адрес на узбекском', widget=forms.Textarea, required=False)
    address_eng = forms.CharField(label='Адрес на английском', widget=forms.Textarea, required=False)

    class Meta:
        model = Branche
        fields = '__all__'
