from django.db import models
from django.contrib.auth.models import User


class Cargo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Cargos'


class Empleado(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='empleado'
    )
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='empleados',
    )

    def __str__(self):
        return self.usuario.first_name + ' ' + self.usuario.last_name

    class Meta:
        verbose_name_plural = 'Empleados'
