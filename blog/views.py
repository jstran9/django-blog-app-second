from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h2>Hi Snickers!</h2>")


def about(request):
    return HttpResponse("<h2>Hi Roxy!!</h2>")

