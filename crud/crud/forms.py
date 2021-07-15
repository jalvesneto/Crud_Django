from django.forms import ModelForm
from Crud_Django.models import Lembrete

class LembreteForm(ModelForm):
    class Meta:
        model = Lembrete
        fields = ['lembrete']