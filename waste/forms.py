from django.forms import ModelForm
from waste.models import Waste

class WasteForm(ModelForm):
    class Meta:
        model = Waste
        fields = ['waste_type','weight']