from django.contrib import admin
from apps.customer.models import Empresa, Departamento, Municipio, PersonaNatural, PersonaJuridica

admin.site.register(Empresa)
admin.site.register(Departamento)
admin.site.register(Municipio)
admin.site.register(PersonaNatural)
admin.site.register(PersonaJuridica)
