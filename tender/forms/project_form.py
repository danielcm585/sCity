from django.forms import ModelForm
from tender.models.project_model import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','description']