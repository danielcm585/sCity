from django.db import models
from tender.models.company import Company
from tender.models.project import Project

class Registrant(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    offer_price = models.IntegerField()
    deal_price = models.IntegerField()
    registered_at = models.DateTimeField(auto_now_add=True)
    is_chosen = models.BooleanField(default=False)