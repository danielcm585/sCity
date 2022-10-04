import datetime
from django.shortcuts import render
from tender.models import Tender

def dashboard(request):
    now = datetime.now()
    tenders = Tender.objects.all() 
    tenders = filter(lambda tender: (now < tender.closed_at), tenders)
    context = {
        'last_login': request.COOKIES.get('last_login'),
        'tenders': tenders
    }
    return render(request, 'tender.html', context)