from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


API_TITLE = 'Activos Fijos - Grupo ASD'
API_DESCRIPTION = 'Activos Fijos'


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^activos-fijos/api/', include('activos_fijos.urls')),
    url(r'^activos-fijos/api/', include('ubicacion.urls')),
    url(r'^activos-fijos/api/', include('empleados.urls')),
    url(r'^activos-fijos/api/v1/docs/', include_docs_urls(
        title=API_TITLE,
        description=API_DESCRIPTION)
        )
]
