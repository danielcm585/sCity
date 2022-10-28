from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    photo = models.TextField() #Ganti foto
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    contact_name = models.TextField()
    contact_number = models.TextField()