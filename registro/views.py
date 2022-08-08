

from django.shortcuts import render, redirect
from registro.forms import usuarioForm, vehiculoForm
from registro.models import Usuario, Vehículo
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# lOGICA DE USUARIO (EDITAR ELIMINAR Y OTRAS FUNCIONES)
@login_required(login_url='/login/')
def usuario(request):
    usuario_db = Usuario.objects.all() #Se carga la base de datos
    formulario = usuarioForm(request.POST or None, request.FILES or None) # se carga el formulario
    url_back = 'usuario' # se define la url de regreso
    nombre_eliminar = 'Usuario'   # se define el nombre de la tabla
    if formulario.is_valid(): # si el formulario es valido
        formulario.save() # se guarda el formulario
        messages.success(request, '¡Usuario registrado exitosamente!') # se muestra un mensaje de exito
        return redirect('vehiculo') # se redirecciona a la url
    context = { # se define el contexto
        'usuario_db': usuario_db,	
        'formulario': formulario,
        'url_back': url_back,
        'nombre_eliminar': nombre_eliminar,
    }
    
    return render (request, 'register/user.html', context) # se renderiza la pagina

def usuariodelete(request,id): # se define la funcion para eliminar un usuario
    delete_user = Usuario.objects.get(id=id) # se obtiene el usuario
    usuario_db = Usuario.objects.all() # se carga la base de datos
    txt_action = 'este usuario' # se define el texto de la accion
    formulario = usuarioForm() # se carga el formulario
    if request.method == 'POST' and 'form1' in request.POST: # si el metodo es post y el formulario es form1
        delete_user.delete() # se elimina el usuario
        messages.success(request,'Usuario %s eliminado exitosamente' %delete_user.nombre) # se muestra un mensaje de exito
        return redirect ('usuario') # se redirecciona a la url
    if request.method == 'POST' and 'form2' in request.POST: # si el metodo es post y el formulario es form2
        return redirect ('usuario') # se redirecciona a la url
    context = {'usuario_db': usuario_db, 'formulario': formulario,'txt_action': txt_action} # se define el contexto
    return render (request,'register/deleteUser.html', context ) # se renderiza la pagina


def editarUsuario(request,id): # se define la funcion para editar un usuario
    edit_user = Usuario.objects.get(id=id) # se obtiene el usuario

    formulario = usuarioForm(request.POST or None, request.FILES or None, instance=edit_user) # se carga el formulario
    if formulario.is_valid() and request.method == 'POST': # si el formulario es valido y el metodo es post
        formulario.save() # se guarda el formulario
        messages.success(request, '¡Usuario %s fue editado exitosamente!' %edit_user.nombre) # se muestra un mensaje de exito
        return redirect('usuario') # se redirecciona a la url
    context = { # se define el contexto
        'formulario': formulario,
        'edit': edit_user,
    }
    return render (request, 'register/user.html', context)  # se renderiza la pagina
     

# LOGICA DE VEHICULO (EDITAR, ELIMINAR  Y OTRAS FUNCIONES)
@login_required(login_url='/login/') # se define la funcion para ver los vehiculos
def vehiculo(request): # se define la funcion para ver los vehiculos
    vehiculo_db = Vehículo.objects.all() # se carga la base de datos para ver los vehiculos
    usuario_db = Usuario.objects.all() # se carga la base de datos para el select de usuario
    vehiculo = vehiculoForm(request.POST or None) # se carga el formulario
    if vehiculo.is_valid(): # si el formulario es valido 
        vehiculo.save() # se guarda el formulario
        messages.success(request,'¡Vehiculo registrado exitosamente!') # se muestra un mensaje de exito
        return redirect('vehiculo') # se redirecciona a la url
    context = { # se define el contexto
        'vehiculo_db': vehiculo_db,
        'vehiculo': vehiculo,
        'usuario_db': usuario_db,
    }
    return render (request, 'register/vehiculo.html', context) # se renderiza la pagina


def editarVehiculo(request,id): # se define la funcion para
    edit_vehiculo = Vehículo.objects.get(id=id) # se obtiene el vehiculo
    formulario_vehiculo = vehiculoForm(request.POST or None, instance=edit_vehiculo) # se carga el formulario
    usuario_db = Usuario.objects.all() # se carga la base de datos para el select de usuario 

    if formulario_vehiculo.is_valid() and request.method == 'POST': # si el formulario es valido y el metodo es post
        formulario_vehiculo.save() # se guarda el formulario
        messages.success(request, '¡Vehiculo %s fue editado exitosamente!' %edit_vehiculo.placa) # se muestra un mensaje de exito
        return redirect('vehiculo') # se redirecciona a la url
    context={ # se define el contexto
        'vehiculo': formulario_vehiculo,
        'edit': edit_vehiculo,
        'usuario_db': usuario_db
    }
    return render (request, 'register/vehiculo.html', context)  # se renderiza la pagina 

def vehiculoDelete(request,id):
    vehiculo_d = Vehículo.objects.get(id=id) # se obtiene el vehiculo
    vehiculo_db = Vehículo.objects.all() # se carga la base de datos para ver los vehiculos
    txt_action = 'este vehiculo' # se define el texto de la accion
    formulario = vehiculoForm() # se carga el formulario
    if request.method == 'POST' and 'form1' in request.POST: # si el metodo es post y el formulario es
        vehiculo_d.delete() # se elimina el vehiculo
        messages.success(request,'Vehiculo %s eliminado exitosamente' %vehiculo_d.placa) # se muestra un mensaje de exito
        return redirect ('vehiculo') # se redirecciona a la url
    if request.method == 'POST' and 'form2' in request.POST: # si el metodo es post y el formulario es form2
        #no se realiza ninguna accion por que el cliente decidio no eliminar el vehiculo
        return redirect ('vehiculo') # se redirecciona a la url
    context = {
        'vehiculo_db': vehiculo_db,
        'formulario': formulario,
        'txt_action': txt_action
        }
    return render (request,'register/deleteUser.html', context )