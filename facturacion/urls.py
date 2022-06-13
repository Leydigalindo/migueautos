from django.urls import path

from facturacion.views import factura

urlpatterns = [
   path('factura/',factura, name='factura'),
]