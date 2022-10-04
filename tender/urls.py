from django.urls import path
from tender.views import *

app_name = 'tender'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]