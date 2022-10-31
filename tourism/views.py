from django.shortcuts import redirect, render
from .forms import PlaceForm
from .models import Place
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def show_tourism(request):
    place = Place.objects.all()
    print (place)
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'place' : place,
        'form' : PlaceForm(),
    }
    return render(request, "tourism.html", context)
    
def add_tourism(request):
    print ("ok2")
    if request.method == 'POST':
        form = PlaceForm(request.POST, request.FILES)
        print (form.is_valid())
        if form.is_valid():
            print ("ok")
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            place = Place(price=price, name=name, description=description)
            place.save()
            return redirect('tourism:show_tourism')

    else:
        form = PlaceForm()

    return render(request, 'create.html', {'form':PlaceForm()})
