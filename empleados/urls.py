from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from empleados.views import CargoViewSet, EmpleadoViewSet, UserViewSet


router = DefaultRouter()
router.register(r'cargos', CargoViewSet, 'cargo')
router.register(r'empleados', EmpleadoViewSet, 'empleado')
router.register(r'users', UserViewSet, 'user')


urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
