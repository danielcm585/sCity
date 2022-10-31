from django.urls import path
from tourism.views import *

app_name = 'tourism'

urlpatterns = [
    path('', show_tourism, name='show_tourism'),
    path('add/', add_tourism, name='add_tourism'),

]