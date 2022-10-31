from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Items(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to="images/")  #Ganti foto
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.BigIntegerField()
    contact_name = models.TextField()
    contact_number = models.TextField()