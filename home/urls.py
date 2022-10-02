from django.urls import path
from home.views import *

app_name = 'home'

urlpatterns = [
    path('', home, name='home')
]