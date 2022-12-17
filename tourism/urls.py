from django.urls import path
from tourism.views import *

app_name = 'tourism'

urlpatterns = [
    path('', show_tourism, name='show_tourism'),
    path('add/', add_tourism, name='add_tourism'),
    path('add_visitor/<int:id>', add_visitor, name='add_visitor'),
    path('delete/', delete_tourism, name='delete_tourism'),
    path('add_visitor_flutter/<int:id>', add_visitor_flutter, name='add_visitor_flutter'),
    path('json', get_tourism_json, name='get_tourism_json'),
    path('add_flutter/', add_tourism_flutter, name='add_tourism_flutter'),
    path('adminCheck',admin_check_api,name='admin_check_api'),
]