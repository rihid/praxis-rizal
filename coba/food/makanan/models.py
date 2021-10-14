from django.db import models
from django.db.models.base import Model


class makanan(models.Model):
    jenis = models.CharField(max_length=255)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()
