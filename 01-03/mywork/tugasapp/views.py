from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse(request, 'index.html')

def about(request):
    return HttpResponse("Halaman About")

    
