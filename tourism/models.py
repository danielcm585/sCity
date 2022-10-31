from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.PositiveIntegerField(default=0)
