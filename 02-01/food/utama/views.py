from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'base.html')


def makanan(request):
    return render(request, 'makanan/index.html')


def minuman(request):
    return render(request, 'minuman/index.html')
