from asyncio.windows_events import NULL
from django.db import models
from django.utils.translation import gettext_lazy as _



class Vehículo(models.Model):
    placa = models.CharField(max_length=7, unique=True, help_text="placa del vehiculo",verbose_name="Placa")
    fecha = models.DateField(verbose_name="Fecha de Registro", help_text=u"MM/DD/AAAA")
    modelo = models.CharField(max_length=25, help_text="modelo del texto")
    color= models.CharField(max_length=15, verbose_name="color del vehículo")
    class Estado(models.TextChoices):
        EXCELENTE = 'E', _('Exelente (E)')
        REGULAR = 'R', _('Regular (R)')
        BIEN = 'B', _('Bien (B)')
        MAL = 'M', _('Mal (M)')
    estado = models.CharField(max_length=10,choices=Estado.choices, verbose_name=u"Estado")
    
    def __str__(self) -> str:
        return '%s %s %s %s %s'%(self.placa, self.fecha, self.estado, self.modelo, self.color)
    


class Usuario(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    apellido = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Apellido")
    telefono = models.CharField(max_length=13, blank=True, unique=True, verbose_name="Numero de celular")
    vehiculo = models.ForeignKey(Vehículo, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return '%s %s'%(self.nombre, self.apellido)
    