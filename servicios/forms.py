from django import forms

from servicios.models import Insumo, Marca, Servicio

class ServicioForm(forms.ModelForm):
    class Meta:
        model= Servicio
        fields='__all__' 
        #fields= '__all__'
class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields='__all__' 
    
        #fields = '__all__'
        
class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields='__all__' 
        #fields = '__all__'
    