from rest_framework import serializers
from tender.models.project_model import Project

class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','title','description','closed_at','is_closed','created_at','edited_at','closed_at']