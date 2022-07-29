
from . import views
from django.urls import path


urlpatterns = [
    path ('factura/',views.factura, name='factura'),
    path ('factura/eliminarfactura/<int:id>',views.eliminarFactura, name='eliminarfactura'),
    path ('factura/editarfactura/<int:id>',views.editarFactura, name='editarFactura'),
]