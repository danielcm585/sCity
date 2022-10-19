from django.shortcuts import render

def dashboard(request):
    context = { 'is_admin': True }
    return render(request, "tender.html", context)