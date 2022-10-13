from rest_framework import serializers
from tender.models.registrant import Registrant
from tender.serializers.company import CompanySerializer

class RegistrantSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    
    class Meta:
        model = Registrant
        fields = ['id','company','project_id','offer_price','deal_price','registered_at']