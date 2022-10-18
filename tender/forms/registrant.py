from django.forms import ModelForm
from tender.models.registrant import Registrant

class RegistrantForm(ModelForm):
    class Meta:
        model = Registrant
        fields = ['company_id']