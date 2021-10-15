from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from makanan.models import makanan
from minuman.models import minuman

# from makanan import models as makanan_models


# class pesanan(models.Model):
#     makanan = models.ForeignKey(
#         makanan_models.makanan, on_delete=models.CASCADE, related_name='pesanan')
#     qty = models.IntegerField(default=1)

class pesanan(models.Model):
    makanan = models.ForeignKey(makanan, on_delete=CASCADE)
    qty_makanan = models.IntegerField()
    minuman = models.ForeignKey(minuman, on_delete=CASCADE)
    qty_minuman = models.IntegerField()
