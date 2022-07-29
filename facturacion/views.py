from django.shortcuts import render, redirect
from facturacion.forms import FacturaForm
from facturacion.models import Factura
from django.contrib.auth.decorators import login_required

from registro.models import Usuario, Vehículo


@login_required(login_url='/login/')
def factura(request):
    usuarios = Usuario.objects.all()
    vehiculos = Vehículo.objects.all()
    factura_db = Factura.objects.all()
    factura = FacturaForm()
    if request.method == 'POST':
       
        factura = FacturaForm(request.POST)
    
        if factura.is_valid():
            factura.save()
            return redirect('factura')
        else:
            print("No es valido")
        
    context = {
        'factura': factura_db,
        'factura_form': factura,
        'usuario': usuarios,
        'vehiculo': vehiculos,
    }
    return render (request, 'facturacion/factura.html', context)


def detallefactura(request, factura):
    cr
    
    pass











def editarFactura(request,id):
    edit_factura = Factura.objects.get(id=id)
    factura  = FacturaForm(request.POST or None, instance=edit_factura)
    
    context={
        'factura': factura ,
    }
    if factura.is_valid() and request.method == 'POST':
        factura .save()
        return redirect('factura')
    return render (request, 'facturacion/factura.html', context)  

def eliminarFactura(request,id):
    factura_d = Factura.objects.get(id=id)
    factura_db = Factura.objects.all()
    formulario = FacturaForm()
    if request.method == 'POST':
        factura_d.delete()
        return redirect ('factura')
    context = {
        'factura_db': factura_db,
        'formulario': formulario,
        }
    return render (request,'facturacion/deletefactura.html', context )    
    