from django.forms import ModelForm

from tender.models import *

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_id', 'pt_name', 'npwn']

class TenderForm(ModelForm):
    class Meta:
        model = Tender
        fields = ['title','description','closed_at']

class RegistrantForm(ModelForm):
    class Meta:
        model = Registrant
        fields = ['offer_price']

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','quantity','description','price']
