from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

from empleados.models import Empleado
from ubicacion.models import CentroCostos


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Categorías'


class TipoActivo(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='tipos_activos',
        blank=True,
        null=True,
        verbose_name='Categoría')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Tipos de activos'


class ActivoFijo(models.Model):
    fecha_compra = models.DateTimeField(
        blank=True,
        null=True
    )
    numero_serial = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Número serial'
    )
    numero_placa = models.CharField(max_length=50, verbose_name='Número placa')
    codigo_rfid = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Código RFID'
    )
    responsable = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='activos'
    )
    centro_costo = models.ForeignKey(
        CentroCostos,
        on_delete=models.CASCADE,
        related_name='activos',
        null=True,
        blank=True
    )
    tipo_activo = models.ForeignKey(
        TipoActivo,
        on_delete=models.CASCADE,
        related_name='activos'
    )

    def __str__(self):
        return self.numero_placa

    class Meta:
        verbose_name_plural = 'Activos fijos'

    def save(self, *args, **kwargs):
        if self.fecha_compra <= timezone.now():
            super(ActivoFijo, self).save(*args, **kwargs)
