from django.shortcuts import render


from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models


def index(request):
    if request.POST:
        inputJenis = request.POST['jenis'],
        inputNama = request.POST['nama'],
        inputHarga = request.POST['harga']
        models.makanan.objects.create(
            jenis=inputJenis, nama=inputNama, harga=inputHarga)
    data = models.makanan.objects.all()
    return render(request, 'pesanan/index.html', {
        'data': data
    })


def updateMakanan(request, id):
    if request.POST:
        models.makanan.objects.filter(pk=id).update(
            inputJenis=request.POST['jenis'],
            inputNama=request.POST['nama'],
            inputHarga=request.POST['harga']
        )
        return redirect('/makanan')

    hasil = models.makanan.objects.filter(pk=id).first()
    print(hasil)
    return render(request, 'makanan/edit.html', {
        'detail_edit': hasil,
    })


def hapusMakanan(request, id):
    models.makanan.objects.filter(pk=id).delete()
    return redirect('/pesanan')
