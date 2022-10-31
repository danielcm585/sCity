from django.db import models
from django.contrib.auth.models import User
from tender.models.image_model import Image

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    company_name = models.CharField(max_length=100)
    pt_name = models.CharField(max_length=200)
    npwp = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)