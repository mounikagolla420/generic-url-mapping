from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first_app2(request):
    return HttpResponse('i love you')


def second_app2(request):
    return HttpResponse('i love you too')