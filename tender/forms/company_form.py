from django.forms import ModelForm
from tender.models.company_model import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name','pt_name','npwp']