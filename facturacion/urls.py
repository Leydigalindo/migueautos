from django.urls import path

from facturacion.views import factura

urlpatterns = [
   path('factura/',factura, name='factura'),
   path('factura/<int:pk>',factura, name='factura'),
   # path('detalle-factura/<int:id>',detallefactura, name='detalle-factura'),
]