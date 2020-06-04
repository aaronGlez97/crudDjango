#aqui se van a crear mis formularios
from django.forms import ModelForm

#importando el modelo que cree 
from appregistro.models import Registro

class RegistroForm(ModelForm):
    class Meta:
        model=Registro
        fields=['id','nombre' ,'correo','telefono','domicilio']
