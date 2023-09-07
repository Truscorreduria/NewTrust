from django import forms
from apps.policy.models import Poliza, Documento


# ------------------------------------------->
# Forms Poliza

class PolizaFrom(forms.ModelForm):
    class Meta:
        model = Poliza
        fields = '__all__'
        labels = {
            'id': 'Id Poliza',
            'ramo': 'Ramo',
            'subramo': 'Sub Ramo',
            'fechaInicio': 'Fecha Inicio',
            'fechaFin': 'Fecha Fin',
            'aseguradora': 'Aseguradora',
            'ejecutivo': 'Ejecutivo',
            'cliente': 'Cliente',
            'contratante': 'Contratante',
            'grupo': 'Grupo',
            'tipo': 'Tipo',
            'concepto': 'Concepto',
            'cesionario': 'Cesionario'
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'ramo': forms.Select(attrs={'class': 'form-control'}),
            'subramo': forms.Select(attrs={'class': 'form-control'}),
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control datepicker', 'autocomplete': 'off'}),
            'aseguradora': forms.Select(attrs={'class': 'form-control'}),
            'ejecutivo': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'contratante': forms.Select(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'concepto': forms.Select(attrs={'class': 'form-control'}),
            'cesionario': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class DocumentoForm(forms.ModelForm):
    class Meta:
        model = Documento
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'poliza': 'Poliza',
            'documento': 'documentacion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'poliza': forms.TextInput(attrs={'class': 'form-control W10', 'readonly': 'True'}),
            'documento': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

