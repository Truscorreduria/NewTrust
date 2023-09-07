from django.contrib import admin

from apps.policy.models import Poliza, Ramo, SubRamo, Grupo, Aseguradora

# Register your models here.
admin.site.register(Poliza)
admin.site.register(Ramo)
admin.site.register(SubRamo)
admin.site.register(Aseguradora)
admin.site.register(Grupo)
