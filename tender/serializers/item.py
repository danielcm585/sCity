from rest_framework import serializers
from tender.serializers import RegistrantSerializer

class ItemSerializer(serializers.ModelSerializer):
    registrant = RegistrantSerializer(read_only=True)
    
    class Meta:
        model = Item
        fields = ['id','registrant','name','quantity','price','description']