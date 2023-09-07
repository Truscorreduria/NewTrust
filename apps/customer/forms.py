from django import forms
from apps.customer.models import PersonaNatural, PersonaJuridica, Empresa

# Formato texto con acentos y otros.
abc = "[A-Za-zñÑáéíóúÁÉÍÓÚüÜllLL ]+"


# ------------------------------------------->
# Forms Persona Natural

class PersonaNaturalFrom(forms.ModelForm):
    class Meta:
        model = PersonaNatural
        fields = '__all__'
        labels = {
            'id': 'Número de cedula',
            'primerNombre': 'Primer Nombre',
            'segundoNombre': 'Segundo Nombre',
            'primerApellido': 'Primer Apellido',
            'segundoApellido': 'Segundo Apellido',
            'genero': 'Genero',
            'estadoCivil': 'Estado civil',
            'identificacion': 'Identificacion',
            'telefono': 'Telefono',
            'correo': 'Correo',
            'departamento': 'Departamento',
            'municipio': 'Municipio',
            'direccion': 'Domicilio',
            'empresa': 'Empresa',
            'documento': 'Documentos'
        }
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'XXX-XXXXXX-XXXXZ'}),
            'primerNombre': forms.TextInput(attrs={'class': 'form-control', 'pattern': abc}),
            'segundoNombre': forms.TextInput(attrs={'class': 'form-control', 'pattern': abc}),
            'primerApellido': forms.TextInput(attrs={'class': 'form-control', 'pattern': abc}),
            'segundoApellido': forms.TextInput(attrs={'class': 'form-control', 'pattern': abc}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estadoCivil': forms.Select(attrs={'class': 'form-control'}),
            'identificacion': forms.Select(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'pattern': '^[0-9]+'}),
            'correo': forms.TextInput(attrs={'class': 'form-control',
                                             'pattern': '[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}$}'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'cols': "40", 'rows': "5"}),
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'documento': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


# ------------------------------------------->
# Forms Persona Juridica

class PersonaJuridicaFrom(forms.ModelForm):
    class Meta:
        model = PersonaJuridica
        fields = '__all__'
        labels = {
            'ruc': 'RUC',
            'razonSocial': 'Razon Social',
            'nombre': 'Nombre',
            'actividadEconomica': 'Actividad Economica',
            'telefono': 'Telefono',
            'web': 'Pagina Web',
            'cesionario': ' Cesionario',
            'departamento': 'Departamento',
            'municipio': 'Municipio',
            'direccion': 'Dirección',
            'representante': 'Representante Legal',
            'documento': 'Documentos'

        }
        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control'}),
            'razonSocial': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'pattern': abc}),
            'actividadEconomica': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'pattern': '^[0-9]+'}),
            'web': forms.TextInput(attrs={'class': 'form-control'}),
            'cesionario': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'cols': "40", 'rows': "5"}),
            'representante': forms.Select(attrs={'class': 'form-control'}),
            'documento': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }


# ------------------------------------------->
# Forms Empresa


class EmpresaFrom(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        labels = {
            'nombre': 'Nombre',
            'direccion': 'Direccion',
            'telefono': 'Telefono'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
