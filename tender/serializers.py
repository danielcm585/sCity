from rest_framework import serializers
from tender.models import Company, Project, Registrant, Item

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','user_id','company_name','pt_name','npwp','created_at','updated_at']

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['id','title',]

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ['photo','temperature','humidity','time','location']

class ItemSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = ['species','logs']
