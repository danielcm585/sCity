from rest_framework import serializers
from tender.models.registrant_model import Registrant

class SimpleRegistrantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrant
        fields = ['id','offer_price','deal_price','registered_at','is_chosen']