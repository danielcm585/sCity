from django.db import models
from tender.models.company_model import Company
from tender.models.project_model import Project

class Registrant(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='registrants')
    offer_price = models.IntegerField(default=0)
    deal_price = models.IntegerField(null=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_chosen = models.BooleanField(default=False)