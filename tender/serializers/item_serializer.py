from rest_framework import serializers
from tender.models.item_model import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id','registrant_id','name','quantity','price','description']