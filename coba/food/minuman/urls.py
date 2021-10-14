from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hapus/<id>', views.hapusMinuman),
    path('update/<id>', views.updateMakanan),
    # path('detail/<id>', views.lihatMakanan),
]
