from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def dashboard(request):
    return render(request, "tender.html")

@login_required(login_url='/authentication/login')
def admin(request):
    # TODO: If not admin -> Forbidden
    return render(request, "tender-admin.html")

def all_companies(request):
    return render(request, "all_companies.html")

def one_company(request, id):
    context = { 'id': id }
    return render(request, "one_company.html", context)

@api_view(['GET','POST'])
def all_companies_json(request):
    def get():
        # Get all companies (Public)
        return ""
    
    def post():
        # Create a new company (User)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','POST'])
def one_company_json(request, id):
    def get():
        # Get company :id details (Public)
        return ""

    def put():
        # Edit company :id (Company)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET','POST'])
def all_projects_json(request):
    def get():
        # Get all projects (Public)
        return ""
    
    def post():
        # Create new project (Admin)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','POST'])
def one_project_json(request, id):
    def get():
        # Get project :id details (Public)
        return ""

    def put():
        # Edit project :id (Admin)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

def all_registrants_json(request, id):
    def get():
        # Get all registrant of project :id (Public)
        return ""
    
    def post():
        # Add new registration to project :id (Company)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

def one_registrant_json(request, id):
    def get():
        # Get registrant :id details (Public)
        return ""
    
    def put():
        # Edit registration :id (Company)
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

