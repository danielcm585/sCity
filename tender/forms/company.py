from django.forms import ModelForm
from tender.models.company import Company

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['company_name','pt_name','npwp']