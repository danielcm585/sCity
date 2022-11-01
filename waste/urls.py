from django.urls import path
from waste.views import *

app_name = 'waste'

urlpatterns = [
    path('', show_home, name='show_waste'),
    path('json/', get_waste_json, name='get_waste_json'),
    path('add/', add_waste, name='add_waste'),
    path('admin/', show_admin, name='show_admin'),
    path('json/admin', get_waste_json_admin, name='get_waste_json_admin'),
    path('admin/update/<int:id>', update_waste, name="update_waste"),
    path('admin/delete/<int:id>', delete_waste, name="delete_waste"),
]