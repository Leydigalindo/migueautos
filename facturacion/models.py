from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from servicios.models import Servicio
from registro.models import Vehículo
class Factura(models.Model):
    vehículo=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Placa')
    class Estado(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')
        ANULADA = 'Anulada', _('Anulada')
    estado = models.CharField(max_length=10, choices=Estado.choices, verbose_name='estado', default=Estado.ACTIVO)
    
    def __str__(self) -> str:
        return '%s'%(self.vehículo)
