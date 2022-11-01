from django.urls import path
from marine.views import *


app_name = 'marine'

urlpatterns = [
    path('', marine_home, name="marine_home"),
    path('admin/', admin_view, name="admin_view"),
    path('delete/<int:pk>/', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', add_item, name='add_task'),
]