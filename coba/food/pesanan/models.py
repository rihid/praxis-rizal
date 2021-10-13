from django.db import models

from makanan import models as makanan_models


class pesanan(models.Model):
    makanan = models.ForeignKey(
        makanan_models.makanan, on_delete=models.CASCADE, related_name='pesanan')
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.makanan.nama

    def total(self):
        return self.makanan.harga * self.qty
