from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from activos_fijos.views import (
    ActivoFijoViewSet,
    CategoriaViewSet,
    TipoActivoViewSet
)


router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, 'categoria')
router.register(r'tipos-activo', TipoActivoViewSet, 'tipo-activo')
router.register(r'activos-fijos', ActivoFijoViewSet, 'activo-fijo')


urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
