from django.urls import path
from waste.views import *

app_name = 'waste'

urlpatterns = [
    path('', show_home, name='show_waste'),
    path('json/', get_waste_json, name='get_waste_json'),
    path('add/', add_waste, name='add_waste'),
    path('api/add/', add_waste_api, name='add_waste_api'),
    path('admin/', show_admin, name='show_admin'),
    path('api/adminCheck/', admin_check_api, name='admin_check_api'),
    path('json/admin', get_waste_json_admin, name='get_waste_json_admin'),
    path('admin/update/<int:id>', update_waste, name="update_waste"),
    path('admin/delete/<int:id>', delete_waste, name="delete_waste"),
    path('api/admin/update/<int:id>', api_update_waste, name="api_update_waste"),
    path('api/admin/delete/<int:id>', api_delete_waste, name="api_delete_waste"),
]