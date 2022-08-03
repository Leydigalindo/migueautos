from dataclasses import field
from django import forms

from facturacion.models import Factura, detalleFactura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['Usuario','vehiculo']
class DetalleForm(forms.ModelForm):
    class Meta:
        model = detalleFactura
        fields = ['servicio', 'insumo', 'total', 'cantidad']
        
        