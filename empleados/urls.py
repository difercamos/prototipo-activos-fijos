from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from empleados.views import CargoViewSet, EmpleadoViewSet


router = DefaultRouter()
router.register(r'cargos', CargoViewSet, 'cargo')
router.register(r'empleados', EmpleadoViewSet, 'empleado')


urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
