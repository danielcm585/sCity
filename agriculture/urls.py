from django.urls import path
from agriculture.views import *


app_name = 'agriculture'

urlpatterns = [
    path('', agriculture_home, name="agriculture_home"),
    # path('admin/', admin_view, name="admin_view"),
    path('delete/<int:pk>/', delete, name='delete'),
    path('json/', show_json, name='show_json'),
    path('add/', add_item, name='add_task'),
    path('single/<int:pk>/', single_view, name='single_view')
]