from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.company_model import Company
from tender.forms.company_form import CompanyForm
from tender.serializers.company_serializer import CompanySerializer

def all_companies(request):
    context = { 
        'last_login': request.COOKIES.get('last_login') 
    }
    return render(request, "all_companies.html", context)

def one_company(request, id):
    context = { 
        'id': id,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "one_company.html", context)

@api_view(['GET','POST'])
def all_companies_api(request):
    def get():
        # Get all companies (Public)
        companies = Company.objects.all()
        companies_serialized = CompanySerializer(instance=companies, many=True)
        return Response(companies_serialized.data, status=status.HTTP_200_OK)
    
    def post():
        # Create a new company (User)
        if (request.user.is_authenticated):
            form = CompanyForm(request.POST)
            if (form.is_valid()):
                new_company = Company.objects.create(
                    user = request.user,
                    company_name = form.cleaned_data.get('company_name'),
                    pt_name = form.cleaned_data.get('pt_name'),
                    npwp = form.cleaned_data.get('npwp'),
                )
                new_company_serialized = CompanySerializer(instance=new_company)
                return Response(new_company_serialized.data, status=status.HTTP_201_CREATED)
            return Response('Input not valid', status=status.HTTP_400_BAD_REQUEST)
        return Response('You must be logged in', status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()
    elif (request.method == 'POST'): return post()

@csrf_exempt
def all_companies_v2_api(request):
    def post():
        # Create a new company (User)
        if (request.user.is_authenticated):
            company_name = request.POST.get('company_name')
            pt_name = request.POST.get('pt_name')
            npwp = request.POST.get('npwp')
            is_valid = (
                company_name != None and len(company_name) > 0 and
                pt_name != None and len(pt_name) > 0 and
                npwp != None and len(npwp) > 0
            )
            if (is_valid):
                new_company = Company.objects.create(
                    user = request.user,
                    company_name = company_name,
                    pt_name = pt_name,
                    npwp = npwp,
                )
                new_company_serialized = CompanySerializer(instance=new_company)
                return JsonResponse({'status': 201, 'data': new_company_serialized.data}, status=201)
            return JsonResponse({'status': 400, 'message': 'Input not valid'}, status=400)
        return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)

    if (request.method == 'POST'): return post()

@api_view(['GET'])
def my_companies_api(request):
    def get():
        if (request.user.is_authenticated):
            companies = Company.objects.filter(user=request.user)
            companies_serialized = CompanySerializer(instance=companies, many=True)
            return Response(companies_serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()

@api_view(['GET','PUT'])
def one_company_api(request, id):
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



