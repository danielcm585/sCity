from django.urls import path
from .views import *

app_name = 'healthcare'
urlpatterns = [
    path('', show_healthcare, name='show_healthcare'),
    path('add/', add_keluhan, name='add_keluhan'),
    path('update/<int:pk>', update_keluhan, name='update_keluhan'),
    path('delete/<int:pk>', delete_keluhan, name='delete_keluhan'),
]