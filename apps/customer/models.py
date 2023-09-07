from django.db import models


# ------------------------------------------------------------------------------------>
# Model Departamento


class Departamento(models.Model):
    departamento = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamento'

    def __str__(self):
        return self.departamento


# ------------------------------------------------------------------------------------>
# Model Municipio


class Municipio(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    municipio = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipio'

    def __str__(self):
        return self.municipio


# ------------------------------------------------------------------------------------>
# Model Empresa


class Empresa(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    direccion = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return self.nombre


# ------------------------------------------------------------------------------------>
# Model Persona Natural


class PersonaNatural(models.Model):
    GENERO = (('Masculino', 'Masculino'), ('Femenino', 'Femenino'))
    ESTADO_CIVIL = (('Soltero', 'Soltero'), ('Casado', 'Casado'))
    IDENTIFICACION = (('Cédula', 'Cédula'), ('Pasaporte', 'Pasaporte'), ('RUC', 'RUC'))
    id = models.CharField(max_length=100, primary_key=True)
    primerNombre = models.CharField(max_length=100, null=True)
    segundoNombre = models.CharField(max_length=100, null=True)
    primerApellido = models.CharField(max_length=100, null=True)
    segundoApellido = models.CharField(max_length=100, null=True)
    genero = models.CharField(max_length=100, null=True, choices=GENERO)
    estadoCivil = models.CharField(max_length=100, null=True, choices=ESTADO_CIVIL)
    identificacion = models.CharField(max_length=100, null=True, choices=IDENTIFICACION)
    telefono = models.CharField(max_length=100, null=True)
    correo = models.EmailField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=100, null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)
    documento = models.FileField(upload_to="persona_natural", null=True)

    class Meta:
        verbose_name = 'Persona Natural'
        verbose_name_plural = 'Persona Natural'

    def __str__(self):
        return '%s %s' % (self.primerNombre, self.primerApellido)


# ------------------------------------------------------------------------------------>
# Model Persona Juridica


class PersonaJuridica(models.Model):
    ruc = models.CharField(max_length=100, primary_key=True)
    razonSocial = models.CharField(max_length=100, null=True)
    nombre = models.CharField(max_length=100, null=True)
    actividadEconomica = models.CharField(max_length=100, null=True)
    telefono = models.CharField(max_length=100, null=True)
    web = models.CharField(max_length=100, null=True)
    cesionario = models.BooleanField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
    direccion = models.CharField(max_length=100, null=True)
    representante = models.ForeignKey(PersonaNatural, on_delete=models.CASCADE, null=True)
    documento = models.FileField(upload_to="persona_juridica", null=True)

    class Meta:
        verbose_name = 'Persona Juridica'
        verbose_name_plural = 'Persona Juridica'

    def __str__(self):
        return self.nombre






# A = PersonaNatural.objects.all().values_list('nombre').union(PersonaJuridica.objects.all().values_list('nombre'))
