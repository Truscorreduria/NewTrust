from django import forms
from apps.payment.models import Recibo, Cuota


# ------------------------------------------->
# Forms Forma de pago

class ReciboFrom(forms.ModelForm):
    class Meta:
        model = Recibo
        fields = '__all__'
        labels = {
            # --------------------------------------------------------->
            'ramo': 'Ramo',
            # --------------------------------------------------------->
            'formaPago': 'Forma de pago',
            'pagoPor': 'Pago por ',
            'cantidadCuotas': 'Cantidad de Cuotas',
            'fecha': 'Fecha Pago',
            'recibo': 'Recibo',
            'poliza': 'Poliza',
            'prima': 'Prima',
            'descuento': 'Descuento',
            'primaNeta': 'Prima Neta',
            'emision': 'Emisión',
            'iva': 'IVA',
            'otrosGastos': 'Otros Gastos',
            'total': 'Total',
            'comision': 'Comisión',
            'porcentajeSubComision': 'Subcomision',
            'montoComision': 'Monto de Comisión ',
            'modenda': 'Moneda'
        }
        widgets = {
            # --------------------------------------------------------->
            'ramo': forms.TextInput(attrs={'class': 'form-control'}),
            # --------------------------------------------------------->
            'formaPago': forms.Select(attrs={'class': 'form-control'}),
            'pagoPor': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidadCuotas': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control', 'type': "date"}),
            'recibo': forms.TextInput(attrs={'class': 'form-control'}),
            'poliza': forms.Select(attrs={'class': 'form-control W10', 'readonly': 'True'}),
            'prima': forms.TextInput(attrs={'class': 'form-control'}),
            'descuento': forms.TextInput(attrs={'class': 'form-control'}),
            'primaNeta': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'emision': forms.TextInput(attrs={'class': 'form-control'}),
            'iva': forms.TextInput(attrs={'class': 'form-control'}),
            'otrosGastos': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'True'}),
            'comision': forms.TextInput(attrs={'class': 'form-control'}),
            'porcentajeSubComision': forms.TextInput(attrs={'class': 'form-control'}),
            'montoComision': forms.TextInput(attrs={'class': 'form-control'}),
            'moneda': forms.Select(attrs={'class': 'form-control'})
        }


class CuotaForm(forms.ModelForm):
    class Meta:
        model = Cuota
        fields = '__all__'  # Agrega los campos necesarios
        labels = {
            'recibo': 'Recibo',
            'poliza': 'Poliza',
            'numero_cuota': 'Numero cuota',
            'fecha': 'Fecha',
            'monto': 'Monto',
            'saldo': 'Saldo',
            'comision': 'Comision',
            'estado': 'Estado',
            'dias_mora': 'Dias Mora'
        }





