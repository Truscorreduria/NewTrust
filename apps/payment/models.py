from datetime import timedelta

from django.db import models

from apps.policy.models import Poliza


# ------------------------------------------------------------------------------------>
# Model Recibo

class Recibo(models.Model):
    MONEDA = (('Cordoba', 'Cordoba'), ('Euro', 'Euro'), ('Dolar', 'Dolar'))
    FORMA_PAGO = (('Contado', 'Contado'), ('Fraccionado', 'Fraccionado'))
    PAGO_POR = (('Transferencia', 'Transferencia'), ('Cheque', 'Cheque'), ('Deposito', 'Deposito'),
                ('Tarjeta De Crédito', 'Tarjeta De Crédito'), ('Deducción Por Nomina', 'Deducción Por Nomina'),
                ('Efectivo', 'Efectivo'))
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE, null=True)
    formaPago = models.CharField(max_length=100, null=True, choices=FORMA_PAGO)
    pagoPor = models.CharField(max_length=100, null=True, choices=PAGO_POR)
    cantidadCuotas = models.IntegerField(null=True)
    fecha = models.DateField(null=True)
    recibo = models.CharField(max_length=100, primary_key=True)
    prima = models.FloatField(null=True)
    descuento = models.FloatField(null=True)
    primaNeta = models.FloatField(null=True)
    emision = models.FloatField(null=True)
    iva = models.FloatField(null=True)
    otrosGastos = models.FloatField(null=True)
    total = models.FloatField(null=True)
    comision = models.FloatField(null=True)
    porcentajeSubComision = models.FloatField(null=True)
    montoComision = models.FloatField(null=True)
    moneda = models.CharField(max_length=100, null=True, choices=MONEDA)

# ------------------------------------------------------------------------------------>
# Model cuota


class Cuota(models.Model):
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE)
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE, null=True)
    numero_cuota = models.IntegerField()
    fecha = models.DateField()
    monto = models.FloatField()
    saldo = models.FloatField()
    comision = models.FloatField()
    estado = models.CharField(max_length=100, default='Pendiente')
    dias_mora = models.IntegerField(default=0)

    def __str__(self):
        return f"Cuota {self.numero_cuota} - Recibo {self.recibo.recibo}"
