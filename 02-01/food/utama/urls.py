from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.makanan),
    path('', views.minuman),
    # path('makanan/', views.makanan),
]
