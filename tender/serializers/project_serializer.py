from rest_framework import serializers
from tender.models.project_model import Project
from tender.serializers.registrant_serializer import RegistrantSerializer

class ProjectSerializer(serializers.ModelSerializer):
    registrants = RegistrantSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id','title','description','closed_at','registrants','is_closed','created_at','edited_at','closed_at']