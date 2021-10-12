from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('makanan/', include('makanan.urls')),
    # path('pesanan/', include('pesanan.urls')),
]
