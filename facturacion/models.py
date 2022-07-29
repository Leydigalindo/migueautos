from django.db import models
from django.utils.translation import gettext_lazy as _

from registro.models import Usuario, Vehículo
from servicios.models import Servicio,Insumo
class Factura(models.Model):    
    fecha=models.DateField(auto_now=True)
    Usuario=models.ForeignKey(Usuario,on_delete=models.SET_NULL, null=True,verbose_name='Usuario') 
    vehiculo = models.ForeignKey(Vehículo,on_delete=models.SET_NULL, null=True, verbose_name='Vehículo')
    class Estadofac(models.TextChoices):
        ACTIVO = 'Activo', _('Activa')
        FINAL = 'Finalizada', _('Finalizada')
    estado = models.CharField(max_length=11,choices=Estadofac.choices,default = Estadofac.ACTIVO, verbose_name=u"Estado")
     
    def __str__(self) -> str:
        return '%s %s %s'%(self.vehiculo,self.fecha, self.Usuario)

class detalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.SET_NULL, null=True, verbose_name='Factura')
    
    servicio = models.ForeignKey(Servicio, on_delete=models.SET_NULL, null=True, verbose_name="servicio")
    insumo = models.ForeignKey(Insumo,on_delete=models.SET_NULL,null=True, verbose_name="Insumo")
    cantidad = models.IntegerField(max_length=7, default=0.00)
    total = models.IntegerField(default=0.00)
    # insumo
    # servicio
    # cantidad
    # total
    