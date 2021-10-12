from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hapus/<id>', views.hapusMakanan),
    path('update/<id>', views.updateMakanan),
]
