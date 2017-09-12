from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from ubicacion.models import CentroCostos
from activos_fijos.models import ActivoFijo
from ubicacion.serializers import CentroCostosSerializer
from activos_fijos.serializers import ActivoFijoSerializer


class CentroCostosViewSet(viewsets.ModelViewSet):
    queryset = CentroCostos.objects.all()
    serializer_class = CentroCostosSerializer

    @detail_route(url_path='activos-fijos')
    def activos_fijos(self, request, pk=None):
        activos_fijos = ActivoFijo.objects.filter(centro_costo=pk)
        serializer = ActivoFijoSerializer(activos_fijos, many=True)
        return Response(serializer.data)
