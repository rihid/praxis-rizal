from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('hapus/<id>', views.hapusMinuman),
    path('update/<id>', views.updateMinuman),
    path('detail/<id>', views.lihatMinuman),
]
