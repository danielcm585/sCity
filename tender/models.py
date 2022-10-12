from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    pt_name = models.CharField(max_length=200)
    npwp = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    closed_at = models.DateTimeField()
    chosen_registrant_id = models.ForeignKey('Registrant', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

class Registrant(models.Model):
    id = models.AutoField(primary_key=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, )
    offer_price = models.IntegerField()
    deal_price = models.IntegerField()
    registered_at = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    registrant_id = models.ForeignKey(Registrant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models
    price = models.IntegerField()
    description = models.TextField()