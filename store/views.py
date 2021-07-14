from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Barcha musiqalar")

def single_news(request):
    return HttpResponse("Bitta musiqa")