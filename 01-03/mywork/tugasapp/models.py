from django.db import models

# Bikin Tabel

class tugas(models.Model):
    nama = models.CharField(max_length=200)