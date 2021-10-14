from django.shortcuts import render, redirect
# from food.makanan import models
from django.http import HttpResponse
from . import models


def index(request):
    if request.POST:
        jenis = request.POST['jenis']
        nama = request.POST['nama']
        harga = request.POST['harga']
        models.minuman.objects.create(jenis=jenis, nama=nama, harga=harga)
    data = models.minuman.objects.all()
    return render(request, 'minuman/index.html', {
        'data': data
    })


def updateMakanan(request, id):
    if request.POST:
        models.minuman.objects.filter(pk=id).update(
            jenis=request.POST['jenis'],
            nama=request.POST['nama'],
            harga=request.POST['harga']
        )
        return redirect('/minuman')
    hasil = models.minuman.objects.filter(pk=id).first()
    print(hasil)
    return render(request, 'minuman/edit.html', {
        'detail_edit': hasil
    })


def hapusMinuman(request, id):
    models.minuman.objects.filter(pk=id).delete()
    return redirect('/minuman')
