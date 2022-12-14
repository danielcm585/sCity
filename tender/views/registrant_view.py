from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.company_model import Company
from tender.models.project_model import Project
from tender.models.registrant_model import Registrant
from tender.forms.registrant_form import RegistrantForm
from tender.serializers.project_serializer import ProjectSerializer
from tender.serializers.registrant_serializer import RegistrantSerializer

def join_tender(request, id):
    context = { 
        'id': id,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "join_tender.html", context)

@api_view(['GET','POST'])
def all_registrants_api(request):
    # TODO: Later
    pass

@api_view(['GET','POST','PUT'])
def one_registrant_api(request, id):
    def get():
        # Get registrant :id details (Public)
        registrant = Registrant.objects.get(id=id)
        registrant_serialized = RegistrantSerializer(instance=registrant)
        return Response(registrant_serialized.data, status=status.HTTP_200_OK)

    def post():
        # Add new registration to project :id (Company) 
        if (request.user.is_authenticated):
            form = RegistrantForm(request.POST)
            if (form.is_valid()):
                company = form.cleaned_data.get('company')
                company = Company.objects.get(id=company.id)
                project = Project.objects.get(id=id)
                project_serialized = ProjectSerializer(instance=project)
                if (company != None and project != None):
                    if (not project.is_closed):
                        is_registered = False
                        print(project_serialized.data)
                        for registrant in project_serialized.data.get('registrants'):
                            if (registrant.get('company').get('id') == company.id):
                                is_registered = True
                        if (not is_registered):
                            new_registrant = Registrant.objects.create(
                                project = project,
                                company = company,
                                offer_price = form.cleaned_data.get('offer_price')
                            )
                            new_registrant_serialized = RegistrantSerializer(instance=new_registrant)
                            return Response(new_registrant_serialized.data, status=status.HTTP_201_CREATED)
                        return Response('You have already registered', status=status.HTTP_400_BAD_REQUEST)
                    return Response('Project is closed', status=status.HTTP_400_BAD_REQUEST)
                return Response('Company or project not found', status=status.HTTP_400_BAD_REQUEST)
            return Response('Input invalid', status=status.HTTP_400_BAD_REQUEST)
        return Response('You are not an admin', status=status.HTTP_401_UNAUTHORIZED)

    def put():
        # Edit registration :id (Company)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()
    elif (request.method == 'POST'): return post()

@csrf_exempt
def one_registrant_v2_api(request, id):
    def post():
        # Add new registration to project :id (Company) 
        # TODO:
        if (request.user.is_authenticated):
            company_id = int(request.POST.get('company_id'))
            offer_price = int(request.POST.get('offer_price'))
            is_valid = (
                company_id != None and
                offer_price != None and offer_price > 0
            )
            if (is_valid):
                company = Company.objects.get(id=company_id)
                project = Project.objects.get(id=id)
                project_serialized = ProjectSerializer(instance=project)
                if (company != None and project != None):
                    if (not project.is_closed):
                        is_registered = False
                        for registrant in project_serialized.data.get('registrants'):
                            if (registrant.get('company').get('id') == company.id):
                                is_registered = True
                        if (not is_registered):
                            new_registrant = Registrant.objects.create(
                                project = project,
                                company = company,
                                offer_price = offer_price
                            )
                            new_registrant_serialized = RegistrantSerializer(instance=new_registrant)
                            return JsonResponse({'status': 201, 'data': new_registrant_serialized.data}, status=201)
                        return JsonResponse({'status': 400, 'message': 'You have already registered'}, status=400)
                    return JsonResponse({'status': 400, 'message': 'Project is closed'}, status=400)
                return JsonResponse({'status': 400, 'message': 'Company or project not found'}, status=400)
            return JsonResponse({'status': 400, 'message': 'Input invalid'}, status=400)
        return JsonResponse({'status': 401, 'message': 'You are not an admin'}, status=400)

    if (request.method == 'POST'): return post()

@api_view(['GET'])
def choose_registrant_api(request, id):
    def get():
        # Choose registrant :id (Admin)
        if (request.user.is_authenticated and request.user.is_superuser):
            registrant = Registrant.objects.get(id=id)
            project = Project.objects.get(id=registrant.project_id)
            if (registrant != None):
                registrant.is_chosen = True
                project.is_closed = True
                project.closed_at = datetime.now()
                registrant.save()
                project.save()
                return Response(status=status.HTTP_200_OK)
            return Response('Registrant not found', status=status.HTTP_404_NOT_FOUND)
        return Response('You are not an admin', status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()

def choose_registrant_v2_api(request, id):
    def get():
        # Choose registrant :id (Admin)
        if (request.user.is_authenticated and request.user.is_superuser):
            registrant = Registrant.objects.get(id=id)
            project = Project.objects.get(id=registrant.project_id)
            if (not project.is_closed):
                if (registrant != None):
                    registrant.is_chosen = True
                    project.is_closed = True
                    project.closed_at = datetime.now()
                    registrant.save()
                    project.save()
                    return JsonResponse({'status': 200, 'message': 'Perusahaan berhasil dipilih'}, status=200)
                return JsonResponse({'status': 404, 'message': 'Registrant not found'}, status=404)
            return JsonResponse({'status': 400, 'message': 'Project is closed'}, status=400)
        return JsonResponse({'status': 401, 'message': 'You are not an admin'}, status=401)

    if (request.method == 'GET'): return get()