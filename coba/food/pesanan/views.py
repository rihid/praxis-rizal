from django.shortcuts import render


from makanan import models as makanan_models
from . import models


def index(request):
    pesanans = makanan_models.makanan.objects.all()
    total = 0
    # for o in pesanans:
    #     total += o.total()
    return render(request, 'pesanan/index.html', {
        'data': pesanans,
        'total': total,
    })
