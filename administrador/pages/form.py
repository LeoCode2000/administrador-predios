from django import forms
from .models import Predio, Propietario, Matricula


class MatriculaForm(forms.Form):

    class Meta:
        model = Matricula        
        fields = ['propietario','predio']


class PropietarioForm(forms.ModelForm):
    nombre = forms.CharField(required=True)
    identificacion = forms.CharField(required=True)

    class Meta:
        model = Propietario
        fields = ("nombre","identificacion")

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['nombre']
            self.fields['identificacion']


class PredioForm(forms.Form):

    class Meta:
        model = Predio
        """cedulaCatastral = forms.CharField(label="Cedula catastral", required=True)
        direccion = forms.CharField(label="Dirección", required=True)
        tipoDePredio = forms.ModelChoiceField(label="Tipo de predio", widget=forms.Select, queryset=Predio.objects.all())"""
        fields = ['cedulaCatastral','direccion', 'tipoDePredio']
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.fields['cedula_catastral']
            self.fields['direccion']
            self.fields['tipoDePredio']
