from django.shortcuts import render

from django.http import HttpResponse
from . import models


def index(request):
    return render(request, 'base.html')


def makanan(request):
    if request.POST:
        input_jenis = request.POST['jenis']
        input_nama = request.POST['nama']
        input_harga = request.POST['harga']
        models.makanan.objects.create(
            jenis=input_jenis, nama=input_nama, harga=input_harga)
    data = models.makanan.objects.all()
    return render(request, 'makanan/index.html')


def minuman(request):
    return render(request, 'minuman/index.html')
