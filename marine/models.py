from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo_url = models.TextField(null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    contact_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)