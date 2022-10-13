from rest_framework import serializers
from tender.models import Project
from tender.serializers import RegistrantSerializer

class ProjectSerializer(serializers.ModelSerializer):
    registrants = RegistrantSerializer(many=True, read_only=True)
    chosen_registrant = RegistrantSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ['id','title','description','closed_at','registrants','chosen_registrant','created_at','edited_at']