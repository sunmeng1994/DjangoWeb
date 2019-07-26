from django.shortcuts import render,get_object_or_404
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

def index(request):
    return HttpResponse("hello,go fuck yourself")