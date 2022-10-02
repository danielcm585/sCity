from django.shortcuts import render

def home(request):
    print("HELO")
    return render(request, "home.html")