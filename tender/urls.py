from django.urls import path
from tender.views import *

app_name = 'tender'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin, name='admin'),
    path('company/', all_companies, name='all_companies'),
    path('company/<int:id>', one_company, name='one_company'),
    path('json/company/', all_companies_json, name='all_companies_json'),
    path('json/company/<int:id>', one_company_json, name='one_company_json'),
    path('json/project/', all_projects_json, name='all_projects_json'),
    path('json/project/<int:id>', one_project_json, name='one_project_json'),
    path('json/registrant/', all_registrants_json, name='all_registrants_json'),
    path('json/registrant/<int:id>', one_registrant_json, name='one_registrant_json'),
]