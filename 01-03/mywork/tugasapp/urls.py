from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hapus/<id>', views.hapus),
    path('update/<id>', views.update),
    path('detail/<id>', views.detail),
]