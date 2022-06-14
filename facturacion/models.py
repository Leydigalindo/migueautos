from django.db import models
from django.utils.translation import gettext_lazy as _
from servicios.models import Servicio
from registro.models import Vehículo
class Factura(models.Model):

    vehículo=models.ForeignKey(Vehículo,on_delete=models.SET_NULL,null=True,related_name='Placa')
         