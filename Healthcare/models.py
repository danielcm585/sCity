from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    disease = models.CharField(max_length=300)
    appointment_date = models.DateTimeField(default=datetime.now, blank=True)
    phone_number = models.CharField(max_length=12)
    appointment_status = models.BooleanField(null=True, blank=True)
    payment_status = models.BooleanField(default=False, null=True, blank=True)

