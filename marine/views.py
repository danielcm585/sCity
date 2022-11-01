from django.shortcuts import *
from marine.models import *
from django.contrib import messages
from django.core import serializers
from .forms import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.db.models.fields.files import ImageFieldFile
from django.urls import reverse
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
        'items_data': data,
        'form': form,
    }
    return render(request, "admin_view.html", context)

def delete(request, pk):
    item = Items.objects.get(id=pk)
    if item:
        item.delete()
        return redirect('marine:admin_view')
        
    messages.error(request, 'Error! Tidak dapat menghapus task')
    return redirect('marine:admin_view')

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

