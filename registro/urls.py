from django.urls import path    
from . import views

urlpatterns = [
    path ('vehiculo/', views.vehiculo, name='vehiculo'),
    path ('vehiculo/eliminarvehiculo/<int:id>', views.vehiculoDelete, name='eliminarvehiculo'),
    path ('vehiculo/editarvehiculo/<int:id>', views.editarVehiculo, name='editarVehiculo'),
    path ('usuario/', views.usuario, name='usuario'),
    path ('usuario/editarusuario/<int:id>', views.editarUsuario, name='editarUsuario'),
    path ('usuario/eliminarusuario/<int:id>', views.usuariodelete, name='eliminarusuario'),
 ]