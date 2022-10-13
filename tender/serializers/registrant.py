from rest_framework import serializers
from tender.models import Registrant
from tender.serializers import CompanySerializer, ProjectSerializer

class RegistrantSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    project = ProjectSerializer(read_only=True)
    
    class Meta:
        model = Registrant
        fields = ['id','company','project','offer_price','deal_price','registered_at']