from django.shortcuts import render
from marine.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def marine_home(request):
    data = Items.objects.all()
    context = {
        'items_data': data,
    }
    return render(request, "marine_home.html", context)

