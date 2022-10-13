from rest_framework import serializers
from tender.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','registrant_id','name','quantity','price','description']