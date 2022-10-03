from django.shortcuts import render

def home(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, "home.html", context)