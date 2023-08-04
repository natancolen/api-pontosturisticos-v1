from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from enderecos.api.viewsets import EnderecoViewSet
from pontosturisticos.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracaoViewSet

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet)
router.register(r'atracoes', AtracaoViewSet)
router.register(r'enderecos', EnderecoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
