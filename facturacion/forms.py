from django import forms

from facturacion.models import Factura

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['Usuario','vehiculo']