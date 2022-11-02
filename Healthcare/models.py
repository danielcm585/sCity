from django.db import models
from django.contrib.auth.models import User

class Healthcare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keluhan = models.CharField(max_length=100, default='')
    appointment_date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=12)
    appointment_status = models.BooleanField(default=False)

