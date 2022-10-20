from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.project_model import Project
from tender.models.registrant_model import Registrant
from tender.serializers.project_serializer import ProjectSerializer
from tender.serializers.registrant_serializer import RegistrantSerializer

def dashboard(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "tender.html", context)

def test(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "test.html", context)

@api_view(['GET'])
def test_registrant(request):
    def get():
        registrants = Registrant.objects.all()
        registrants_serialized = RegistrantSerializer(instance=registrants, many=True)
        return Response(registrants_serialized.data, status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()

@api_view(['GET'])
def test_project(request):
    def get():
        projects = Project.objects.all()
        projects_serialized = ProjectSerializer(instance=projects, many=True)
        return Response(projects_serialized.data, status=status.HTTP_200_OK)

    if (request.method == 'GET'): return get()