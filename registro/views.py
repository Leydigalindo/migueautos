
from multiprocessing import context
from django.shortcuts import render, redirect
from registro.forms import usuarioForm, vehiculoForm
from registro.models import Usuario, Vehículo
from django.contrib.auth.decorators import login_required
# Create your views here.


# lOGICA DE USUARIO (EDITAR ELIMINAR Y OTRAS FUNCIONES)
@login_required(login_url='/login/')
def usuario(request):
    usuario_db = Usuario.objects.all()
    formulario = usuarioForm(request.POST or None, request.FILES or None)
    url_back = 'usuario'
    nombre_eliminar = 'Usuario'
    if formulario.is_valid():
        formulario.save()
        return redirect('usuario')
    context = {
        'usuario_db': usuario_db,	
        'formulario': formulario,
        'url_back': url_back,
        'nombre_eliminar': nombre_eliminar,
    }
    
    return render (request, 'register/user.html', context)

def usuariodelete(request,id):
    delete_user = Usuario.objects.get(id=id)
    usuario_db = Usuario.objects.all()
    txt_action = 'este usuario'
    formulario = usuarioForm()
    if request.method == 'POST' and 'form1' in request.POST:
        delete_user.delete()
        return redirect ('usuario')
    if request.method == 'POST' and 'form2' in request.POST:
        return redirect ('usuario')
    context = {'usuario_db': usuario_db, 'formulario': formulario,'txt_action': txt_action}
    return render (request,'register/deleteUser.html', context )


def editarUsuario(request,id):
    edit_user = Usuario.objects.get(id=id)
    formulario = usuarioForm(request.POST or None, request.FILES or None, instance=edit_user)
    context = {
        'formulario': formulario,
    }
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('usuario')
    return render (request, 'register/user.html', context) 
     

# LOGICA DE VEHICULO (EDITAR, ELIMINAR  Y OTRAS FUNCIONES)
@login_required(login_url='/login/')
def vehiculo(request):
    vehiculo_db = Vehículo.objects.all()
    vehiculo = vehiculoForm(request.POST or None)
    if vehiculo.is_valid():
        vehiculo.save()
        return redirect('vehiculo')
    context = {
        'vehiculo_db': vehiculo_db,
        'vehiculo': vehiculo,
    }
    return render (request, 'register/vehiculo.html', context)


def editarVehiculo(request,id):
    edit_vehiculo = Vehículo.objects.get(id=id)
    formulario_vehiculo = vehiculoForm(request.POST or None, instance=edit_vehiculo)
    
    context={
        'vehiculo': formulario_vehiculo,
    }
    if formulario_vehiculo.is_valid() and request.method == 'POST':
        formulario_vehiculo.save()
        return redirect('vehiculo')
    return render (request, 'register/vehiculo.html', context)  

def vehiculoDelete(request,id):
    vehiculo_d = Vehículo.objects.get(id=id)
    vehiculo_db = Vehículo.objects.all()
    txt_action = 'este vehiculo'
    formulario = vehiculoForm()
    if request.method == 'POST':
        vehiculo_d.delete()
        return redirect ('vehiculo')
    context = {
        'vehiculo_db': vehiculo_db,
        'formulario': formulario,
        'txt_action': txt_action
        }
    return render (request,'register/deleteUser.html', context )