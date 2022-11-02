from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Waste(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, default='')
    date = models.DateField(auto_now_add=True)
    weight = models.PositiveIntegerField(default=0)
    is_confirm = models.BooleanField(default=False)
    waste_type = models.CharField(max_length=100)
