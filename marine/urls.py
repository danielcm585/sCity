from django.urls import path
from marine.views import *


app_name = 'marine'

urlpatterns = [
    path('', marine_home, name="marine_home"),
    path('admin/', admin_view, name="admin_view")
]