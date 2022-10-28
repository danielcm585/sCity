from rest_framework import serializers
from tender.models.registrant_model import Registrant
from tender.serializers.simple_project_serializer import SimpleProjectSerializer

class SimpleRegistrantSerializer(serializers.ModelSerializer):
    project = SimpleProjectSerializer()

    class Meta:
        model = Registrant
        fields = ['id','offer_price','registered_at','is_chosen','project']