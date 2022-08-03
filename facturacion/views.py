from datetime import datetime
from django.shortcuts import render, redirect
from facturacion.forms import DetalleForm, FacturaForm
from facturacion.models import Factura, detalleFactura
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from registro.models import Usuario, Vehículo

from datetime import datetime

@login_required(login_url='/login/')
def factura(request):
    # logica 2 (prueba)
    factura_db = Factura.objects.all()
    usuarios = Usuario.objects.all()
    vehiculos = Vehículo.objects.all()
    time = datetime.now()
                    
    if request.method == 'POST':
        factura = FacturaForm(request.POST)
        print(request.POST)
        if factura.is_valid():
            usuario = Usuario.objects.get(id = request.POST['Usuario'])
            aux = Factura.objects.create(
                fecha = time.strftime("%d/%m/%y %H:%M:%S"),
                Usuario = usuario,
                )
            messages.success(request, f'Factura agregada corretamente.')
            print('se ah logrado hacer la factura ')

            return redirect('detallefactura',aux.id)
        else:
            print("formulario invalido")
    else:
        print(f'No entra')
        messages.warning(request, f'Ups! Parece que no estas generando una factura')
        factura = FacturaForm()

    context = {
        'form': factura,
        'factura_db': factura_db,
        'usuario': usuarios,
        'vehiculo': vehiculos,
    }
    return render(request, 'facturacion/factura.html', context)

    #logica 1(funcional )############################
    # usuarios = Usuario.objects.all()              #
    # vehiculos = Vehículo.objects.all()
    #         factura.save()
    #         return redirect('factura')
    #     else:
    #         print("No es valido")
    # context = {
    #     'factura': factura_db,
    #     'factura_form': factura,
    #     'usuario': usuarios,
    #     'vehiculo': vehiculos,
    #############################################


def detallefactura(request, pk):
    detalle = detalleFactura.objects.filter(factura_id=pk)
    factura_u = Factura.objects.get(id=pk)

    if request.method == 'POST':
        form = DetalleForm(request.POST)
        if form.is_valid():
            factura = detalleFactura.objects.create(
            )
    context = {}
    return render(request, 'facturacion/detalle.html', context)


def editarFactura(request, id):
    edit_factura = Factura.objects.get(id=id)
    factura = FacturaForm(request.POST or None, instance=edit_factura)

    context = {
        'factura': factura,
    }
    if factura.is_valid() and request.method == 'POST':
        factura .save()
        return redirect('factura')
    return render(request, 'facturacion/factura.html', context)


def eliminarFactura(request, id):
    factura_d = Factura.objects.get(id=id)
    factura_db = Factura.objects.all()
    formulario = FacturaForm()
    if request.method == 'POST':
        factura_d.delete()
        return redirect('factura')
    context = {
        'factura_db': factura_db,
        'formulario': formulario,
    }
    return render(request, 'facturacion/deletefactura.html', context)
