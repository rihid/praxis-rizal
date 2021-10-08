from django.shortcuts import render, redirect

from django.http import HttpResponse

from . import models


def index(request):
    if request.POST:

        data = request.POST['fname']
        print(data)
        # Input data ke database
        models.tugas.objects.create(nama = data)
    # Nampilin data
    hasil = models.tugas.objects.all()
    
    return render(request, 'index.html', {'isi': hasil})

# Detail
def detail(request, id):
    data = models.tugas.objects.filter(pk = id).first()
    print(data)
    return render(request, 'detail.html', {
        'dataDetail' : data
    })

# Hapus
def hapus(request, id):
    models.tugas.objects.filter(pk = id).delete()
    return redirect('/')

# Edit
def update(request, id):
    if request.POST:
        input = request.POST['fname']
        print(input)
        models.tugas.objects.filter(pk = id).update(nama = input)
        return redirect('/')
        
    # Nampilin data
    hasil = models.tugas.objects.filter(pk = id).first()
    print(hasil)
    return render(request, 'edit.html', {
        'detailEdit' : hasil,
    })
    
