from django.forms import ModelForm
from tender.models.registrant_model import Registrant

class RegistrantForm(ModelForm):
    class Meta:
        model = Registrant
        fields = ['company']