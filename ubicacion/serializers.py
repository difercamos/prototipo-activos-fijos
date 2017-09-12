from rest_framework import serializers

from ubicacion.models import CentroCostos


class CentroCostosSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCostos
        fields = ('id', 'nombre')
