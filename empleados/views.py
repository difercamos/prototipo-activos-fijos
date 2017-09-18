from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.contrib.auth.models import User

from empleados.models import Cargo, Empleado
from activos_fijos.models import ActivoFijo
from empleados.serializers import (
    CargoSerializer,
    EmpleadoSerializer,
    UserSerializer
)
from activos_fijos.serializers import ActivoFijoSerializer


class CargoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

    @detail_route(url_path='activos-fijos')
    def activos_fijos(self, request, pk=None):
        activos_fijos = ActivoFijo.objects.filter(responsable=pk)
        serializer = ActivoFijoSerializer(activos_fijos, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
