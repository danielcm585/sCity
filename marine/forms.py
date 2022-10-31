from dataclasses import field
from django.forms import ModelForm
from marine.models import Items

class AdminForm(ModelForm):
    class Meta:
        model = Items
        fields = '__all__'