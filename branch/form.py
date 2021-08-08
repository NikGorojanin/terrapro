from django.forms import ModelForm

from api.models import Branche


class BranchForm(ModelForm):
    class Meta:
        model = Branche
        fields = '__all__'
