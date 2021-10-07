from django.shortcuts import render

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
    # return render(request, 'index.html')

def about(request):
    return HttpResponse("Halaman About")

    
