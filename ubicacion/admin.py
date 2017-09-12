from django.contrib import admin

from ubicacion.models import CentroCostos


@admin.register(CentroCostos)
class CentroCostosAdmin(admin.ModelAdmin):
    pass
