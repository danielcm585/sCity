from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

def dashboard(request):
    return render(request, "tender.html")

@login_required(login_url='/authentication/login')
def admin(request):
    # If not admin -> Forbidden
    return render(request, "tender-admin.html")

def all_companies(request):
    return render(request, "all_companies.html")

def one_company(request, id):
    context = { 'id': id }
    return render(request, "one_company.html", context)

@api_view(['GET','POST'])
def all_companies_json(request):
    def get():
        return ""
    
    def post():
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','POST'])
def one_company_json(request, id):
    def get():
        return ""

    def put():
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()

@api_view(['GET','POST'])
def all_projects_json(request):
    def get():
        return ""
    
    def post():
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@api_view(['GET','POST'])
def one_project_json(request, id):
    def get():
        return ""

    def put():
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()