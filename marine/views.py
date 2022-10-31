from django.shortcuts import render
from marine.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def marine_home(request):
    data = Items.objects.all()
    context = {
        'items_data': data,
    }
    return render(request, "marine_home.html", context)

def admin_view(request):
    data = Items.objects.all()
    form = AdminForm()
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'items_data': data,
        'form': form,
    }
    return render(request, "admin_view.html", context)

