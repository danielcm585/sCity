from rest_framework import serializers
from tender.models.company_model import Company

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ['id','photo','user','company_name','pt_name','npwp','projects','created_at','updated_at']