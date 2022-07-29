from django.contrib import admin
from facturacion.models import Factura, detalleFactura

# Register your models here.
admin.site.register(Factura)
admin.site.register(detalleFactura)