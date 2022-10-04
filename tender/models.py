from django.db import models
from authentication.models import User
from tender.models import Registrant

class Company(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    pt_name = models.CharField(max_length=200)
    npwp = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tender(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    closed_at = models.DateTimeField()
    chosen_registrant = models.OneToOneField(Registrant, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

class Registrant(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    tender_id = models.ForeignKey(Tender, on_delete=models.CASCADE)
    offer_price = models.IntegerField()
    deal_price = models.IntegerField()
    registered_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    registrant_id = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models
    price = models.IntegerField()
    description = models.TextField()