from datetime import datetime
from django.shortcuts import render, redirect
from django.db import models
from facturacion.forms import DetalleForm, FacturaForm
from facturacion.models import Factura, detalleFactura
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from registro.models import Usuario, Vehículo
from servicios.models import Servicio,Insumo

from datetime import datetime

from servicios.models import Insumo


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
            usuario = Usuario.objects.get(id=request.POST['Usuario'])
            vehiculo = Vehículo.objects.get(id=request.POST['vehiculo'])
            aux = Factura.objects.create(
                fecha=time.strftime("%d/%m/%y %H:%M:%S"),
                Usuario=usuario,
                vehiculo=vehiculo,
            )
            messages.success(request, f'Factura agregada corretamente.')
            print('se ah logrado hacer la factura ')

            return redirect('detallefactura', aux.id)
        else:
            print("formulario invalido")
    else:
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


def detallefactura(request, pk):  # pk es el id de la factura
    titulo_pagina = "facturas"
    detalles = detalleFactura.objects.filter(factura_id=pk)
    factura_u = Factura.objects.get(id=pk)

    servicio_db = Servicio.objects.all()
    insumo_db = Insumo.objects.all()
    
    
    # Suma los precios y da un total
    if(detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(total_definitivo=Sum(('total'), output_field=models.IntegerField()))):
        total = detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(
            total_definitivo=Sum(('total'), output_field=models.IntegerField()))[0]["total_definitivo"]
    else:
        total = 0
    # Filtrando productos para visualizacion del cliente

    if request.method == 'POST':
        form= DetalleForm(request.POST)
        if form.is_valid():
            producto = Insumo.objects.get(id=request.POST['insumo'])
            if factura_u.estado == "Activo":
                existe = detalleFactura.objects.filter(
                    factura=pk, insumo_id=producto)
                if len(existe) == 0:
                    detalleFactura.objects.create(
                        cantidad=form.cleaned_data.get('cantidad'),
                        total=producto.precioUnitario *
                        form.cleaned_data.get('cantidad'),
                        factura=factura_u,
                        insumo=producto,
                    )
                    print('Parte uno')
                    print('********************* \n')
                    
                    Insumo.objects.filter(id=producto.id).update(
                        cantidad=producto.cantidad -
                        form.cleaned_data.get('cantidad')

                    )
                    print('Parte dos')
                    print('********************* \n')
                    if(detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(total_definitivo=Sum(('total'), output_field=models.IntegerField()))):
                        total = detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(
                            total_definitivo=Sum(('total'), output_field=models.IntegerField()))[0]["total_definitivo"]
                        Factura.objects.filter(id=pk).update(
                            total=total
                        )
                    else:
                        total = 0

                    messages.success(
                        request, f' se agregó {producto} a la factura correctamente!')
                    return redirect('verfactura', pk=pk)
                else:
                    anterior = detalleFactura.objects.filter(
                        factura_id=pk, insumo_id=request.POST['insumo'])

                    detalleFactura.objects.filter(factura_id=pk, insumo_id=request.POST['insumo']).update(
                        cantidad=anterior[0].cantidad +
                        form.cleaned_data.get('cantidad'),
                        total=anterior[0].total + producto.precioUnitario *
                        form.cleaned_data.get('cantidad'),
                    )

                    Insumo.objects.filter(id=producto.id).update(
                        cantidad=producto.cantidad-
                        form.cleaned_data.get('cantidad')

                    )
                    if(detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(total_definitivo=Sum(('total'), output_field=models.IntegerField()))):
                        total = detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(
                            total_definitivo=Sum(('total'), output_field=models.IntegerField()))[0]["total_definitivo"]
                        Factura.objects.filter(id=pk).update(
                            total=total
                        )
                    else:
                        total = 0

                    Factura.objects.filter(id=pk).update(
                        total=total
                    )

            else:
                if(producto.cantidad >= int(request.POST['cantidad'])):
                    existe = detalleFactura.objects.filter(
                        factura_id=factura_u.id, producto=producto)
                    cantidadA = Usuario.objects.filter(id=factura_u)
                    print(cantidadA)
                    if len(existe) == 0:

                        factura = detalleFactura.objects.create(
                            cantidad=form.cleaned_data.get('cantidad'),
                            total=producto.precioUnitario *
                            form.cleaned_data.get('cantidad'),
                            factura=factura_u,
                            insumo=producto,
                        )

                        Insumo.objects.filter(id=producto.id).update(
                            stock=producto.stock -
                            form.cleaned_data.get('cantidad')

                        )

                        if(detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(total_definitivo=Sum(('total'), output_field=models.IntegerField()))):
                            total = detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(
                                total_definitivo=Sum(('total'), output_field=models.IntegerField()))[0]["total_definitivo"]
                            Factura.objects.filter(id=pk).update(
                                total=total
                            )
                        else:
                            total = 0

                        messages.success(
                            request, f' se agregó {producto} a la factura correctamente!')
                        return redirect('factura-detalle', pk=pk)
                    else:
                        anterior = detalleFactura.objects.filter(
                            factura_id=factura_u.id, producto=request.POST['insumo'])

                        anterior.update(
                            cantidad=anterior[0].cantidad -
                            form.cleaned_data.get('cantidad'),
                            total=anterior[0].total + producto.precioUnitario *
                            form.cleaned_data.get('cantidad'),
                        )
                        Insumo.objects.filter(id=producto.id).update(
                            stock=producto.stock -
                            form.cleaned_data.get('cantidad')
                        )
                        if(detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(total_definitivo=Sum(('total'), output_field=models.IntegerField()))):
                            total = detalleFactura.objects.filter(factura_id=factura_u.id).values("factura").annotate(
                                total_definitivo=Sum(('total'), output_field=models.IntegerField()))[0]["total_definitivo"]
                            Factura.objects.filter(id=pk).update(
                                total=total
                            )
                        else:
                            total = 0
                else:
                    messages.warning(
                        request, f' Solo hay stock de {producto.stock} {producto.nombre}/s')
        else:
            messages.warning(request, f' Error')
    else:
        form = DetalleForm()
    context = {
        "titulo_pagina": titulo_pagina,
        "detalles": detalles,
        "form": form,
        "factura": factura_u,
        "total": total,
        "servicios": servicio_db,
        "insumos":  insumo_db,
    }
    return render(request, "facturacion/detalle.html", context)


def viewFac(request, pk): # se genera la vista para ver los detalles de cada factura 
    factura = Factura.objects.get(id=pk) 
    detail = detalleFactura.objects.filter(factura_id=pk)
    print(detail)
    context = {
        "facturas": factura,
        "detalles": detail,
    }
    return render(request, 'facturacion/verfactura.html', context)


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
