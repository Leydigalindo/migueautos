
from . import views
from django.urls import path


urlpatterns = [
    path ('factura/',views.factura, name='factura'),
    path('detallefactura/<int:pk>',views.detallefactura, name='detallefactura'),
    path('verfactura/<int:pk>/',views.viewFac, name='verfactura'),
    
    
    path ('factura/eliminarfactura/<int:id>',views.eliminarFactura, name='eliminarfactura'),
    path ('factura/editarfactura/<int:id>',views.editarFactura, name='editarFactura'),
]