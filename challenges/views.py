from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def january(request):
    return HttpResponse("Eat no sugar for the entire month!")


def february(request):
    return HttpResponse("Walk for at least 30 minutes every day!")


def march(request):
    return HttpResponse("Create a perpetual motion machine!")
