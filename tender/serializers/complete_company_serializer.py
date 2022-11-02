from rest_framework import serializers
from tender.models.company_model import Company
from tender.serializers.registrant_serializer import SimpleRegistrantSerializer

class CompleteCompanySerializer(serializers.ModelSerializer):
    projects = SimpleRegistrantSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id','user','company_name','pt_name','npwp','projects','created_at','updated_at']