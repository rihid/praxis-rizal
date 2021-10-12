from django.db import models
from django.db.models.base import Model


class makanan(models.Model):
    jenis = models.TextField(blank=True, null=True)
    nama = models.TextField(blank=True, null=True)
    harga = models.IntegerField()
    # cek = models.TextField(blank=True, null=True)
