from multiprocessing import context
from django.shortcuts import *
from marine.models import *
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
def marine_home(request):
    data = Items.objects.all()
    if request.user.is_authenticated and request.user.is_superuser:
        data = Items.objects.all()
        form = AdminForm()
        if request.method == "POST":
            form = AdminForm(request.POST, request.FILES )
            if form.is_valid():
                form.save()


        for item in data:
            # if item:
            #     item.delete()
            if isinstance(item.photo, ImageFieldFile):
                item.photo_url = str(item.photo.url)
            item.save()

        context = {
            'last_login': request.COOKIES.get('last_login'),
            'items_data': data,
            'form': form,
            'user': request.user,
        }
        return render(request, "admin_view.html", context)
        

    context = {
        'last_login': request.COOKIES.get('last_login'),
        'items_data': data,
        'user': request.user,
    }
    return render(request, "marine_home.html", context)

# def admin_view(request):
#     data = Items.objects.all()
#     form = AdminForm()
#     if request.method == "POST":
#         form = AdminForm(request.POST, request.FILES )
#         if form.is_valid():
#             form.save()
#             print(form.data)


#     for item in data:
#         # if item:
#         #     item.delete()
#         if isinstance(item.photo, ImageFieldFile):
#             item.photo_url = str(item.photo.url)
#         item.save()

#     context = {
#         'last_login': request.COOKIES.get('last_login'),
#         'items_data': data,
#         'form': form,
#     }
#     return render(request, "admin_view.html", context)

def delete(request, pk):
    item = Items.objects.get(id=pk)
    if item:
        item.delete()
        return redirect('marine:marine_home')
        
    messages.error(request, 'Error! Tidak dapat menghapus task')
    return redirect('marine:marine_home')

def show_json(request):
    data = Items.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        photo = request.POST.get('photo')
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        contact_name = request.POST.get('contact_name')
        contact_number = request.POST.get('contact_number')
        item = Items.objects.create(photo=photo, title=title, description=description, price=price, contact_name=contact_name, contact_number=contact_number)
        result = {
            'pk':item.pk,
            'fields':{
                'photo':item.photo,
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



@csrf_exempt
def delete_flutter(request):
    print("a")
    data = json.loads(request.body)
    print()
    print(data)
    getTitle = data['title']
    getName = data['name']
    getDesc = data['description']
    getNumber = data["contact_number"]
    getPrice = data["price"]
    getUrl = data["photo_url"]
    
    Items.objects.get(title=getTitle, name=getName, description=getDesc, contact_number = getNumber,  price = getPrice, photo_url = getUrl).delete()
    return JsonResponse({"status": "success"}, status=200)
   