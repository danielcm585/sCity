from django.shortcuts import render
from waste.models import Waste
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from waste.forms import WasteForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/authentication/login/')
def show_home(request):
    user_logged_in = request.user
    waste = Waste.objects.filter(user=user_logged_in)
    context = {
        'last_login': request.COOKIES.get('last_login'),
    }
    return render(request, "waste.html", context)

#@login_required(login_url='/authentication/login/')
@csrf_exempt
def add_waste(request):
    if request.method == 'POST':
        if (request.user.is_authenticated):
            form = WasteForm(request.POST)
            if form.is_valid():
                jenis = form.cleaned_data.get('waste_type')
                berat = form.cleaned_data.get('weight')
                username = request.user
                new_waste = Waste(user=request.user,username=username, waste_type=jenis, weight=berat)
                new_waste.save()
                return HttpResponse(b"CREATED", status=201)
        return Response('You must be logged in', status=status.HTTP_401_UNAUTHORIZED)
    return HttpResponseNotFound()

#@login_required(login_url='/authentication/login/')

@csrf_exempt
def add_waste_api(request):
    def post():
        if (request.user.is_authenticated):
            print("masuk")
            waste_type = request.POST.get('waste_type')
            weight = float(request.POST.get('weight'))
            username = request.user
            new_waste = Waste(user=request.user,username=username, waste_type=waste_type, weight=weight)
            new_waste.save()
            return JsonResponse({'status': 201}, status=201)
        return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)
    if (request.method == 'POST'): return post()

def admin_check_api(request):
    def get():
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return JsonResponse({'status': 201, 'message': 'Admin'}, status=201)
            return JsonResponse({'status': 402, 'message': 'You are not admin'}, status=402)
        return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)
    if (request.method == 'GET'): return get()

def get_waste_json(request):
    if (request.method == 'GET'):
        if (request.user.is_authenticated):
            wastes = Waste.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', wastes), content_type='application/json')
        return Response(status=status.HTTP_401_UNAUTHORIZED)

#@login_required(login_url='/authentication/login/')
def get_waste_json_admin(request):
    if (request.user.is_authenticated):
        wastes = Waste.objects.all()
        return HttpResponse(serializers.serialize('json', wastes), content_type='application/json')
    return Response(status=status.HTTP_401_UNAUTHORIZED)



@csrf_exempt
@login_required(login_url='/authentication/login/')
def update_waste(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            waste = Waste.objects.get(pk=id)
            waste.is_confirm = not waste.is_confirm
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

@csrf_exempt
def api_update_waste(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                waste = Waste.objects.get(pk=id)
                waste.is_confirm = not waste.is_confirm
                waste.save()
                return JsonResponse({'status': 201, 'message': 'OK'}, status=201)
            return JsonResponse({'status': 403, 'message': 'Invalid Access'}, status=403)
        return JsonResponse({'status': 402, 'message': 'You are not admin'}, status=402)
    return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)

@csrf_exempt
def api_delete_waste(request, id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == 'POST':
                waste = Waste.objects.get(pk=id)
                waste.delete()
                return JsonResponse({'status': 201, 'message': 'OK'}, status=201)
            return JsonResponse({'status': 403, 'message': 'Invalid Access'}, status=402)
        return JsonResponse({'status': 402, 'message': 'You are not admin'}, status=402)
    return JsonResponse({'status': 401, 'message': 'You must be logged in'}, status=401)



@login_required(login_url='/authentication/login/')
def show_admin(request):
    if request.user.is_superuser:
        waste = Waste.objects.all()
        context = {
            'last_login': request.COOKIES.get('last_login'),
        }
        return render(request, "admin.html", context)
    return HttpResponse("sorry, you are not admin.")