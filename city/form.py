from django.forms import ModelForm

from api.models import Cite


class CityForm(ModelForm):
    class Meta:
        model = Cite
        fields = '__all__'
