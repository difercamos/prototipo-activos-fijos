from rest_framework import viewsets

from activos_fijos.models import ActivoFijo, Categoria, TipoActivo
from activos_fijos.serializers import (
    ActivoFijoSerializer,
    CategoriaSerializer,
    TipoActivoSerializer
)


class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class TipoActivoViewSet(viewsets.ModelViewSet):
    queryset = TipoActivo.objects.all()
    serializer_class = TipoActivoSerializer


class ActivoFijoViewSet(viewsets.ModelViewSet):
    queryset = ActivoFijo.objects.all()
    serializer_class = ActivoFijoSerializer
