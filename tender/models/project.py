from django.db import models
from tender.models import Registrant

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    closed_at = models.DateTimeField()
    chosen_registrant_id = models.ForeignKey(Registrant, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)