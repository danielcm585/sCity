import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("home:home"))
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Username atau Password salah")

    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "login.html", context)

def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun telah berhasil dibuat")
            return redirect("authentication:login")
    
    print(request)
    context = { 
        "form": form,
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("authentication:login"))
    response.delete_cookie("last_login")
    return response

@csrf_exempt
def login_api(request):
    if (request.method == 'POST'):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"status": True, "message": "Login berhasil"}, status=200)
        return JsonResponse({"status": False, "message": "User tidak ditemukan atau password salah"}, status=401)

@csrf_exempt
def register_api(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": True, "message": "Register berhasil"}, status=200)
        return JsonResponse({"status": False, "message": "Registrasi gagal"}, status=401)

@csrf_exempt
def logout_api(request):
    logout(request)
    return JsonResponse({
        'status': True,
        'message': 'Logout berhasil'
    })