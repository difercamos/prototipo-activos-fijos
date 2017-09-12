from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from ubicacion.views import CentroCostosViewSet


router = DefaultRouter()
router.register(r'centros-costos', CentroCostosViewSet, 'centro-costos')


urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
