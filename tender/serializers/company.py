from rest_framework import serializers
from tender.models.company import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','user_id','company_name','pt_name','npwp','created_at','updated_at']