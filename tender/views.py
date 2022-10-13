from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.forms.project import ProjectForm
from tender.models.company import Company
from tender.models.project import Project
from tender.models.registrant import Registrant
from tender.forms.company import CompanyForm
from tender.serializers.company import CompanySerializer
from tender.serializers.project import ProjectSerializer
from tender.serializers.registrant import RegistrantSerializer

# def dashboard(request):
#     return render(request, "tender.html")

# def all_companies(request):
#     return render(request, "all_companies.html")

# def one_company(request, id):
#     context = { 'id': id }
#     return render(request, "one_company.html", context)

# def one_project(request, id):
#     context = { 'id': id }
#     return render(request, "one_project.html", context)

@api_view(['GET','POST'])
def all_companies_json(request):
    def get():
        # Get all companies (Public)
        companies = Company.objects.all()
        companies_serialized = CompanySerializer(instance=companies, many=True)
        return Response(companies_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create a new company (User)
        if (request.user.is_authenticated):
            form = CompanyForm(request.POST)
            new_company = Company.objects.create(
                user = request.user,
                company_name = form.cleaned_data.get('company_name'),
                pt_name = form.cleaned_data.get('pt_name'),
                npwp = form.cleaned_data.get('npwp'),
            )
            new_company_serialized = CompanySerializer(instance=new_company)
            return Response(new_company_serialized.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def one_company_json(request, id):
    def get():
        # Get company :id details (Public)
        company = Company.objects.get(id=id)
        company_serialized = CompanySerializer(instance=company)
        return Response(company_serialized.data, status=status.HTTP_200_OK)

    def put():
        # Edit company :id (Company)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET','POST'])
def all_projects_json(request):
    def get():
        # Get all projects (Public)
        projects = Project.objects.all()
        projects_serialized = ProjectSerializer(instance=projects, many=True)
        return Response(projects_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create new project (Admin)
        if (request.user.is_authenticated):
            # TODO: Check admin
            form = ProjectForm(request.POST)
            new_project = Project.objects.create(
                title = form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description'),
            )
            new_project_serialized = ProjectSerializer(instance=new_project)
            return Response(new_project_serialized.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def one_project_json(request, id):
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

@api_view(['GET','POST'])
def all_registrants_json(request, id):
    def get():
        # Get all registrant of project :id (Public)
        registrants = Registrant.objects.filter(project_id=id)
        registrants_serialized = RegistrantSerializer(instance=registrants, many=True)
        return Response(registrants_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Add new registration to project :id (Company)
        if (request.user.is_authenticated):
            # TODO: Check company id
            return Response(_, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','PUT'])
def one_registrant_json(request, id):
    def get():
        # Get registrant :id details (Public)
        registrant = Registrant.objects.get(id=id)
        registrant_serialized = RegistrantSerializer(instance=registrant)
        return Response(registrant_serialized.data, status=status.HTTP_200_OK)
    
    def put():
        # Edit registration :id (Company)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

