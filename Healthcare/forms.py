from django import forms
from .models import Healthcare

class Form(forms.ModelForm):
    class Meta:
        model = Healthcare
        fields = ['keluhan', 'appointment_date', 'phone_number']