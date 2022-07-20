from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from proyectoUno.models import Edificio, Departamento

# Form Edificio
class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'apellido', 'edad', 'nacionalidad']
        labels = {
            'nombre': _('Ingrese el nombre del Edificio por favor'),
            'apellido': _('Ingrese la direccion por favor'),
            'edad': _('Ingrese la ciudad por favor'),
            'nacionalidad': _('Ingrese el tipo de Edificio por favor'),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['costo', 'numCuartos', 'numbanios', 'propietario']
    
    
    
# Form DepartamentoEdificio
class DepartamentoEdificioForm(ModelForm):
    
    def __init__(self, edificio, *args, **kwargs):
        super(DepartamentoEdificioForm, self).__init__(*args, **kwargs)
        self.initial['edificio'] = edificio
        self.fields["edificio"].widget = forms.widgets.HiddenInput()
        print(edificio)

    