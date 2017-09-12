from django.contrib import admin

from activos_fijos.models import ActivoFijo, TipoActivo, Categoria


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoActivo)
class TipoActivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria')


@admin.register(ActivoFijo)
class ActivoFijoAdmin(admin.ModelAdmin):
    list_display = (
        'fecha_compra',
        'numero_serial',
        'numero_placa',
        'responsable',
        'centro_costo'
    )
