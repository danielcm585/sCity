from django.shortcuts import redirect, render
from .forms import PlaceForm
from .models import Place
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import  HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='/authentication/login/')
def show_tourism(request):
    place = Place.objects.all()
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'place': place,
        'form': PlaceForm(),
    }
    return render(request, "tourism.html", context)


@login_required(login_url='/authentication/login/')
def add_tourism(request):
    if request.user.is_superuser:
        if request.method == 'POST':
                form = PlaceForm(request.POST, request.FILES)
                print(form.is_valid())
                if form.is_valid():
                    name = form.cleaned_data['name']
                    description = form.cleaned_data['description']
                    price = form.cleaned_data['price']
                    image = form.cleaned_data['image']
                    place = Place(price=price, name=name,
                                description=description, image=image)
                    place.save()
                    return redirect('tourism:show_tourism')
        else:
            form = PlaceForm()

        context = {
        'last_login': request.COOKIES.get('last_login'),
        'form': PlaceForm(),
        }
        return render(request, 'create.html', context)
    HttpResponseNotFound

# @login_required(login_url='/authentication/login/')
def get_tourism_json(request):
    place = Place.objects.all()
    return HttpResponse(serializers.serialize('json', place), content_type='application/json')

@login_required(login_url='/authentication/login/')
def add_visitor(request, id):
    response = {}
    if request.method == 'GET':
        place = Place.objects.get(pk=id)
        place.visitor = place.visitor + 1
        place.save()
        response['visitor'] = place.visitor
        return JsonResponse(response)
        
@csrf_exempt
def add_visitor_flutter(request, id):
    response = {}
    if request.method == 'GET':
        place = Place.objects.get(pk=id)
        place.visitor = place.visitor + 1
        place.save()
        response['visitor'] = place.visitor
        return JsonResponse({
            'status': True,
            'message': 'Visitor Berhasil ditambahkan!',
        }, status=200)
       
@csrf_exempt
def delete_tourism(request):
     Place.objects.all().delete()
     return JsonResponse({
            'status': True,
            'message': 'Place Berhasil dihapus!',
        }, status=200)

@csrf_exempt
def add_tourism_flutter(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        image = request.POST.get("image")
        place = Place(price=price, name=name,
                                description=description, image=image)
        place.save()
        return JsonResponse({
            'status': True,
            'message': 'Data Berhasil ditambahkan!',
        }, status=200)   

def admin_check_api(request):
    def get():
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return JsonResponse({'status': 201, 'message': 'Admin'}, status=201)
            return JsonResponse({'status': 402, 'message': 'You are not admin'}, status=402)
        return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)
    if (request.method == 'GET'): return get()             

