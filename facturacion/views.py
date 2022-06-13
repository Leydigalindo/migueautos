from django.shortcuts import redirect, render
from facturacion.forms import FacturaForm
from facturacion.models import Factura
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def factura(request):
    factura_db = Factura.objects.all()
    factura= FacturaForm(request.POST or None, request.FILES or None)
    if factura.is_valid():
        factura.save()
        return redirect('factura')
    context = {
        'factura_db': factura_db,	
        'factura': factura,
    }
    return render (request, 'facturacion/factura.html', context)


