from django.shortcuts import redirect, render
from facturacion.forms import FacturaForm
from facturacion.models import Factura
from django.contrib.auth.decorators import login_required
from facturacion.models import Factura
from servicios.forms import InsumoForm, ServicioForm
from servicios.views import insumo, servicio


@login_required(login_url='/login/')
def factura(request,pk=0):
    factura= FacturaForm(request.POST or None, request.FILES or None)
    vehiculo_fac = ""
    if pk != 0: 
        vehiculo_fac = Factura.objects.get(id=pk) 
#generar factura
    if request.method == 'POST':
        factura.is_valid()
        aux = factura.save()
        pk = aux.id
        vehiculo_fac = pk.vehículo
        print('Factura abierta')
        return redirect ('factura',pk)
    
    context = {
        'factura': factura,
        'servicio': servicio,
        'forminsumo': insumo,
        'vehiculo': vehiculo_fac,
    }
    return render (request, 'facturacion/factura.html', context)

# def detallefactura(request,id):
#      factura= Factura.objects.get(id=id)
#      print('la factura es: ', factura)
#      vehiculo_fac = factura.vehículo
#      context = {
#          'vehiculo_fac' : vehiculo_fac
#      }
#      return render (request, 'facturacion/detalle-factura.html',context)
