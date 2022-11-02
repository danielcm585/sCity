from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from .models import Healthcare
from .forms import Form
from django.core import serializers

@login_required(login_url='/authentication/login/')
def show_healthcare(request):
    user = request.user
    data = Healthcare.objects.all()
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'form': Form()
    }
    return render(request, "Healthcare.html", context)

@login_required(login_url='/authentication/login/')
def add_keluhan(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            keluhan = form.cleaned_data['keluhan']
            phone_number = form.cleaned_data['phone_number']
            Healthcare.objects.create(keluhan=keluhan, phone_number=phone_number, appointment_status=True)
            return HttpResponse({'status': 'success'})
    return HttpResponse({'status': 'failed'})

@csrf_exempt
@login_required(login_url='/authentication/login/')
def update_keluhan(request, pk):
    if request.user.is_superuser:
        if request.method == 'POST':
            healthcare = Healthcare.objects.get(id=pk)
            healthcare.appointment_status = not healthcare.appointment_status
            healthcare.save()
            return redirect('healthcare:show_healthcare')
        return HttpResponseNotFound()
    return HttpResponse("sorry, you are not admin.")

@csrf_exempt
@login_required(login_url='/authentication/login/')
def delete_keluhan(request, pk):
    if request.user.is_superuser:
        if request.method == 'DELETE':
            Healthcare.objects.filter(id=pk).delete()
        return HttpResponse({'status': 'project deleted'})
