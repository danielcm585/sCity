from rest_framework import serializers
from tender.models import Company
from tender.serializers import RegistrantSerializer

class CompanySerializer(serializers.ModelSerializer):
    registrations = RegistrantSerializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['id','user_id','company_name','pt_name','npwp','registrations','created_at','updated_at']