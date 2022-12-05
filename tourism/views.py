from django.shortcuts import redirect, render
from .forms import PlaceForm
from .models import Place
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import  HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers


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

@login_required(login_url='/authentication/login/')
def get_tourism_json_admin(request):
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

