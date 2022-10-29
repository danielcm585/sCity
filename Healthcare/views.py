from django.shortcuts import render
import json
from http.client import HTTPResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from Healthcare.models import Service
from Healthcare.forms import Form

@login_required(login_url='../../login/')
@csrf_exempt
def add_disease(request):
    form = Form()