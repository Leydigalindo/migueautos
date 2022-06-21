from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _

from registro.models import Usuario, Vehículo
class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO = 'Activo', _('Activo')
        INACTIVO = 'Inactivo', _('Inactivo')
        ANULADA = 'Anulada', _('Anulada')
    estado = models.CharField(max_length=10, choices=Estado.choices, verbose_name='estado', default=Estado.ACTIVO)
    
    def __str__(self) -> str:
        return '%s'%(self.usuario)
