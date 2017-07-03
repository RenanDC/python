from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^list/', alocacao_list, name='listar_alocacao'),
    url(r'^alocacao_new/', alocacao_new, name='alocacao_new'),
    url(r'^alocacao_edit/(?P<pk>[0-9]+)', alocacao_edit, name='alocacao_edit'),
    url(r'^alocacao_remove/(?P<pk>[0-9]+)', alocacao_remove, name='alocacao_remove')
]
