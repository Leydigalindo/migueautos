from django.shortcuts import redirect, render
from facturacion.forms import FacturaForm
from facturacion.models import Factura
from django.contrib.auth.decorators import login_required
from servicios.forms import ServicioForm,InsumoForm
from servicios.views import insumo
@login_required(login_url='/login/')
def factura(request):
    factura= FacturaForm(request.POST or None, request.FILES or None)
    servicio = ServicioForm(request.POST or None, request.FILES or None)
    insumo = InsumoForm(request.POST or None, request.FILES or None)
    if factura.is_valid():
        factura.save()
        print('factura abierta')

    context = {
        'factura': factura,
        'servicio': servicio,
        'insumo': insumo
    }
    return render (request, 'facturacion/factura.html', context)


