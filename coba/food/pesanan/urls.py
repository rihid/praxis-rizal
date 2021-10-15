from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hapus/<id>', views.hapusPesanan),
    path('detail/<id>', views.detailPesanan),
    path('edit/<id>', views.editPesanan),
]
