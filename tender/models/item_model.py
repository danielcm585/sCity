from django.db import models
from tender.models.registrant_model import Registrant

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    registrant = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models
    price = models.IntegerField()
    description = models.TextField()