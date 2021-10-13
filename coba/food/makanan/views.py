from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def index(request):
    if request.POST:
        jenis = request.POST['jenis'],
        nama = request.POST['nama'],
        harga = request.POST['harga']
        models.makanan.objects.create(
            jenis=jenis, nama=nama, harga=harga)
    data = models.makanan.objects.all()
    return render(request, 'makanan/index.html', {
        'data': data
    })


def updateMakanan(request, id):
    if request.POST:
        models.makanan.objects.filter(pk=id).update(
            jenis=request.POST['jenis'],
            nama=request.POST['nama'],
            harga=request.POST['harga']
        )
        return redirect('/makanan')

    hasil = models.makanan.objects.filter(pk=id).first()
    print(hasil)
    return render(request, 'makanan/edit.html', {
        'detail_edit': hasil,
    })


def lihatMakanan(request, id):
    data = models.makanan.objects.filter(pk=id).first()
    print(data)
    return render(request, 'makanan/detail.html', {
        'data_detail': data
    })


def hapusMakanan(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/makanan')
