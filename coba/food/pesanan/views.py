from django.shortcuts import render, redirect

# from makanan import models as makanan_models
from . import models


# def index(request):
#     pesanans = makanan_models.makanan.objects.all()
#     total = 0
#     # for o in pesanans:
#     #     total += o.total()
#     return render(request, 'pesanan/index.html', {
#         'data': pesanans,
#         # 'total': total,
#     })

def index(request):
    if request.POST:
        get_makanan = request.POST['makanan']
        get_minuman = request.POST['minuman']
        get_qty_makanan = request.POST['qty_makanan']
        get_qty_minuman = request.POST['qty_minuman']

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman,
                                      qty_makanan=get_qty_makanan, qty_minuman=get_qty_minuman)

    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.all()
    print(data)
    return render(request, "pesanan/index.html", {
        "dataMakanan": dataMakanan,
        "dataMinuman": dataMinuman,
        "data": data,
    })


def detailPesanan(request, id):
    data = models.pesanan.objects.filter(pk=id).first()
    print(data)
    return render(request, 'pesanan/detail.html', {
        'data_detail': data
    })


def editPesanan(request, id):
    if request.POST:
        get_makanan = request.POST['makanan']
        get_minuman = request.POST['minuman']
        get_qty_makanan = request.POST['qty_makanan']
        get_qty_minuman = request.POST['qty_minuman']

        input_makanan = models.makanan.objects.filter(id=get_makanan).first()
        input_minuman = models.minuman.objects.filter(id=get_minuman).first()
        models.pesanan.objects.create(makanan=input_makanan, minuman=input_minuman,
                                      qty_makanan=get_qty_makanan, qty_minuman=get_qty_minuman)
        return redirect('pesanan/')
    dataMakanan = models.makanan.objects.all()
    dataMinuman = models.minuman.objects.all()
    data = models.pesanan.objects.filter(pk=id).first()
    return render(request, 'pesanan/edit.html', {
        'dataMakanan': dataMakanan,
        'dataMinuman': dataMinuman,
        'data': data
    })


def hapusPesanan(request, id):
    models.pesanan.objects.filter(id=id).delete()
    return redirect('/pesanan/')
