from django.test import TestCase
from django.utils import timezone

from activos_fijos.models import ActivoFijo, Categoria, TipoActivo


class ActivoFijoModelTests(TestCase):
    def setUp(self):
        categoria = Categoria.objects.create(nombre='Equipo de computo')
        tipo_activo = TipoActivo.objects.create(
            nombre='Laptop',
            categoria=categoria
        )
        ActivoFijo.objects.create(
            fecha_compra=timezone.now(),
            numero_placa='000001',
            tipo_activo=tipo_activo
        )

    def test_fecha_creacion_futuro(self):
        activo_fijo = ActivoFijo.objects.get(numero_placa='000001')

        self.assertEqual(activo_fijo.numero_placa, '000001')

#  + datetime.timedelta(days=2)
