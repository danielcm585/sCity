from rest_framework import serializers
from tender.models.registrant_model import Registrant
from tender.serializers.company_serializer import CompanySerializer

class RegistrantSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    
    class Meta:
        model = Registrant
        fields = ['id','company','offer_price','deal_price','registered_at']