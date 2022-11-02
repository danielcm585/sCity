from dataclasses import field
from django.forms import ModelForm
from agriculture.models import Items
from django import forms

class AdminForm(ModelForm):
    class Meta:
        model = Items
        fields = ["title", "description", "photo_url", "price", "contact_name", "contact_number"]