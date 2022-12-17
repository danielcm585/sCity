from multiprocessing import context
from django.shortcuts import *
from agriculture.models import *
from django.contrib import messages
from django.core import serializers
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.db.models.fields.files import ImageFieldFile
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
# Create your views here.

#request.user.is_authenticated
#request.user.is_superuser
@login_required(login_url='/authentication/login/')
def agriculture_home(request):
    data = Items.objects.all()
    if request.user.is_authenticated and request.user.is_superuser:
        data = Items.objects.all()
        form = AdminForm()
        if request.method == "POST":
            form = AdminForm(request.POST, request.FILES )
            if form.is_valid():
                form.save()
        # for item in data:
        #     if item:
        #         item.delete()
        context = {
            'last_login': request.COOKIES.get('last_login'),
            'items_data': data,
            'form': form,
            'user': request.user,
        }
        return render(request, "admin2_view.html", context)
        

    context = {
        'last_login': request.COOKIES.get('last_login'),
        'items_data': data,
        'user': request.user,
    }
    return render(request, "agriculture_home.html", context)

def delete(request, pk):
    item = Items.objects.get(id=pk)
    if item:
        item.delete()
        return redirect('agriculture:agriculture_home')
        
    messages.error(request, 'Error! Tidak dapat menghapus task')
    return redirect('agriculture:agriculture_home')

def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        photo_url = request.POST.get('photo_url')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        contact_name = request.POST.get('contact_name')
        contact_number = request.POST.get('contact_number')
        item = Items.objects.create(photo_url=photo_url, title=title, description=description, price=price, contact_name=contact_name, contact_number=contact_number)
        result = {
            'pk':item.pk,
            'fields':{
                'photo_url':item.photo_url,
                'title':item.title,
                'description':item.description,
                'price': item.price,
                'contact_name': item.contact_name,
                'contact_number': item.contact_number,
            }
        }
        return JsonResponse(result)    
    return HttpResponseBadRequest()

def single_view(request, pk):
    data = Items.objects.get(id= pk)
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'item': data,
        'user': request.user,
    }
    return render(request, "single_view.html", context)

@csrf_exempt
def add_flutter(request):
    if request.method == 'POST':
        # Items.objects.all().delete()
        data = json.loads(request.body)
        title = data["title"]
        description = data["description"]
        contact_name = data["contact_name"]
        contact_number = data["contact_number"]
        price = data["price"]
        photo_url = data["photo_url"]
        addItem = Items.objects.create(
            title = title, 
            description = description,
            contact_name = contact_name,
            contact_number = contact_number, 
            price = price, 
            photo_url = photo_url, 
        )
        addItem.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
