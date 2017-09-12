from rest_framework import serializers

from activos_fijos.models import ActivoFijo, Categoria, TipoActivo


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre')


class TipoActivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActivo
        fields = ('id', 'nombre', 'categoria')


class ActivoFijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivoFijo
        fields = (
            'id',
            'fecha_compra',
            'numero_serial',
            'numero_placa',
            'codigo_rfid',
            'responsable',
            'centro_costo',
            'tipo_activo'
        )
