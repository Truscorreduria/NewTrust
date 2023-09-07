from django.db import models


# ------------------------------------------------------------------------------------>
# Model Ramo

class Ramo(models.Model):
    Nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Ramo'
        verbose_name_plural = 'Ramo'

    def __str__(self):
        return self.Nombre


# ------------------------------------------------------------------------------------>
# Model Sub Ramo

class SubRamo(models.Model):
    Ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, null=True)
    Nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Sub Ramo'
        verbose_name_plural = 'Sub Ramo'

    def __str__(self):
        return self.Nombre


# ------------------------------------------------------------------------------------>
# Model Aseguradora

class Aseguradora(models.Model):
    Nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Aseguradora'
        verbose_name_plural = 'Aseguradora'

    def __str__(self):
        return self.Nombre


# ------------------------------------------------------------------------------------>
# Model Grupo

class Grupo(models.Model):
    Nombre = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupo'

    def __str__(self):
        return self.Nombre


# ------------------------------------------------------------------------------------>
# Model Poliza

class Poliza(models.Model):
    TIPO_POLIZA = (('Individual', 'Individual'), ('Colectiva', 'Colectiva'), ('Oficio', 'Oficio'))
    CONCEPTO_POLIZA = (('Nueva póliza', 'Nueva póliza'), ('Renovación', 'Renovación'))
    id = models.CharField(max_length=100, primary_key=True)
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE, null=True)
    subramo = models.ForeignKey(SubRamo, on_delete=models.CASCADE, null=True)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()
    aseguradora = models.ForeignKey(Aseguradora, on_delete=models.CASCADE, null=True)
    ejecutivo = models.CharField(max_length=100, null=True)
    cliente = models.CharField(max_length=100, null=True)
    contratante = models.CharField(max_length=100, null=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=True)
    tipo = models.CharField(max_length=100, null=True, choices=TIPO_POLIZA)
    concepto = models.CharField(max_length=100, null=True, choices=CONCEPTO_POLIZA)
    cesionario = models.BooleanField()

    class Meta:
        verbose_name = 'Poliza'
        verbose_name_plural = 'Poliza'

    def __str__(self):
        return self.id


# ------------------------------------------------------------------------------------>
# Model documento Poliza

class Documento(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    poliza = models.ForeignKey(Poliza, on_delete=models.CASCADE, null=True)
    documento = models.FileField(upload_to="persona_natural", null=True)

    class Meta:
        verbose_name = 'Poliza'
        verbose_name_plural = 'Poliza'

    def __str__(self):
        return self.id


