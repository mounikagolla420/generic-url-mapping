from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_app1(request):
    return HttpResponse('i love my self')

def second_app1(request):
    return HttpResponse('hoo very good')