
from unicodedata import decimal
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Servicio(models.Model):
    class Tipodeservicio (models.TextChoices):
        EXCELENTE = 'Latoneria', _('Latoneria')
        REGULAR= 'Pintura', _('Pintura')
    tipodeservicio = models.CharField(max_length=10, choices=Tipodeservicio.choices, verbose_name=u"Seleccione el tipo de servicio")
    descripcion= models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Descripción")
    def __self__(self) -> str:
        return '%s'%(self.nombre)

class Marca(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    
    def __str__(self) -> str:
            return '%s'%(self.nombre)
class Insumo(models.Model):
    nombre = models.CharField(max_length=45, blank=False, unique= False, verbose_name=u"Nombre")
    cantidad= models.PositiveIntegerField(validators=[MinValueValidator(1)])
    precioUnitario= models.IntegerField(default='0', verbose_name="Precio")
    marca=models.ForeignKey(Marca,on_delete=models.SET_NULL, null=True,verbose_name=u"Marca")

    def __str__(self) -> str:
            return '%s'%(self.nombre)