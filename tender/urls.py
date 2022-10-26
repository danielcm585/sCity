from django.urls import path
from tender.views.general_view import *
from tender.views.company_view import *
from tender.views.project_view import *
from tender.views.registrant_view import *

app_name = 'tender'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('test/', test, name='test'),
    path('test/project/', test_project, name='test_project'),
    path('test/registrant/', test_registrant, name='test_registrant'),
    path('company/', all_companies, name='all_companies'),
    path('company/<int:id>/', one_company, name='one_company'),
    path('project/', all_projects, name='all_projects'),
    path('project/<int:id>/', one_project, name='one_project'),
    path('registrant/<int:id>/', join_tender, name='join_tender'),
    path('api/company/', all_companies_api, name='all_companies_api'),
    path('api/company/<int:id>/', one_company_api, name='one_company_api'),
    path('api/company/mine/', my_companies_api, name='my_companies_api'),
    path('api/project/', all_projects_api, name='all_projects_api'),
    path('api/project/<int:id>/', one_project_api, name='one_project_api'),
    path('api/registrant/', all_registrants_api, name='all_registrants_api'),
    path('api/registrant/<int:id>/', one_registrant_api, name='one_registrant_api'),
    path('api/registrant/choose/<int:id>/', choose_registrant_api, name='choose_registrant_api'),
<<<<<<< HEAD
=======
    path('api/item/', item_api, name='item_api'),
>>>>>>> f3f435f (Push new features)
]