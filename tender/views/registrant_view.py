from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tender.models.company_model import Company
from tender.models.project_model import Project
from tender.models.registrant_model import Registrant
from tender.forms.registrant_form import RegistrantForm
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
                if (company != None):
                    new_registrant = Registrant.objects.create(
                        project = project,
                        company = company,
                        offer_price = form.cleaned_data.get('offer_price')
                    )
                    new_registrant_serialized = RegistrantSerializer(instance=new_registrant)
                    return Response(new_registrant_serialized.data, status=status.HTTP_201_CREATED)
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put():
        # Edit registration :id (Company)
        # TODO: Later
        return ""

    if (request.method == 'GET'): return get()
    elif (request.method == 'PUT'): return put()
    elif (request.method == 'POST'): return post()

@api_view(['GET'])
def choose_registrant_api(request, id):
    def get():
        # Choose registrant :id (Admin)
        if (request.user.is_authenticated and request.user.is_superuser):
            registrant = Registrant.objects.get(id=id)
            registrant.isChosen = True
            registrant.save()
            registrant_serialized = RegistrantSerializer(instance=registrant)
            return Response(registrant_serialized.data, status=status.HTTP_200_OK)
        return Response('You are not admin', status=status.HTTP_401_UNAUTHORIZED)

    if (request.method == 'GET'): return get()