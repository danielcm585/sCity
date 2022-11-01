from django.shortcuts import render
from waste.models import Waste
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from waste.forms import WasteForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='/authentication/login/')
def show_home(request):
    user_logged_in = request.user
    waste = Waste.objects.filter(user=user_logged_in)
    context = {
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, "waste.html", context)

@login_required(login_url='/authentication/login/')
def add_waste(request):
    if request.method == 'POST':
        form = WasteForm(request.POST)
        if form.is_valid():
            jenis = form.cleaned_data.get('waste_type')
            berat = form.cleaned_data.get('weight')
            username = request.user
            new_waste = Waste(user=request.user,username=username, waste_type=jenis, weight=berat)
            new_waste.save()
            return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@login_required(login_url='/authentication/login/')
def get_waste_json(request):
    wastes = Waste.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', wastes), content_type='application/json')

@login_required(login_url='/authentication/login/')
def get_waste_json_admin(request):
    wastes = Waste.objects.all()
    return HttpResponse(serializers.serialize('json', wastes), content_type='application/json')

@csrf_exempt
@login_required(login_url='/authentication/login/')
def update_waste(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            waste = Waste.objects.get(pk=id)
            waste.is_confirm = True
            print(waste)
            waste.save()
            return HttpResponse(b"UPDATED", status=201)
        return HttpResponseNotFound()
    return HttpResponse("sorry, you are not admin.")

@csrf_exempt
@login_required(login_url='/authentication/login/')
def delete_waste(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            waste = Waste.objects.get(pk=id)
            waste.delete()
            return HttpResponse(b"DELETE", status=201)
        return HttpResponseNotFound()
    return HttpResponse("sorry, you are not admin.")

@login_required(login_url='/authentication/login/')
def show_admin(request):
    if request.user.is_superuser:
        waste = Waste.objects.all()
        context = {
            'last_login': request.COOKIES.get('last_login'),
        }
        return render(request, "admin.html", context)
    return HttpResponse("sorry, you are not admin.")