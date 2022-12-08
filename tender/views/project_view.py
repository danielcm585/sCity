import json
from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.project_model import Project
from tender.forms.project_form import ProjectForm
from tender.serializers.project_serializer import ProjectSerializer

def all_projects(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "all_projects.html", context)

def one_project(request, id):
    context = { 
        'id': id,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "one_project.html", context)

@api_view(['GET','POST'])
def all_projects_api(request):
    def get():
        # Get all projects (Public)
        projects = Project.objects.all()
        projects_serialized = ProjectSerializer(instance=projects, many=True)
        return Response(projects_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create new project (Admin)
        if (request.user.is_authenticated and request.user.is_superuser):
            form = ProjectForm(request.POST)
            print(form.is_valid())
            if (form.is_valid()):
                new_project = Project.objects.create(
                    title = form.cleaned_data.get('title'),
                    description = form.cleaned_data.get('description'),
                )
                new_project_serialized = ProjectSerializer(instance=new_project)
                return Response(new_project_serialized.data, status=status.HTTP_201_CREATED)
            return Response('Input not valid', status=status.HTTP_400_BAD_REQUEST)
        return Response('You are not admin', status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@csrf_exempt
def all_projects_v2_api(request):
    def post():
        # Create new project (Admin)
        if (request.user.is_authenticated and request.user.is_superuser):
            title = request.POST.get('title')
            description = request.POST.get('description')
            is_valid = (
                title != None and len(title) > 0 and 
                description != None and len(description) > 0
            )
            if (is_valid):
                new_project = Project.objects.create(title=title, description=description)
                new_project_serialized = ProjectSerializer(instance=new_project)
                return JsonResponse({'status': 200, 'data': new_project_serialized.data}, status=200)
            return JsonResponse({'status': 400, 'meessage': 'Input not valid'}, status=400)
        return JsonResponse({'status': 401, 'message': 'You are not admin'}, status=401)

    if (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def one_project_api(request, id):
    def get():
        # Get project :id details (Public)
        project = Project.objects.get(id=id)
        project_serialized = ProjectSerializer(instance=project)
        return Response(project_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit project :id (Admin)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()