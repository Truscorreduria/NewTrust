from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.policy.views import PolizaList, PolizaCreate, Get_Name_Client, PolizaUpdate, PolizaDelete, \
    DocumentoCreate, DocumentoList

app_name = 'policy'

urlpatterns = [
    # -------------------------------------------------------->
    # Path Poliza
    path('polizaList', login_required(PolizaList.as_view()), name='poliza_list'),
    path('polizaCreate', login_required(PolizaCreate.as_view()), name='poliza_create'),
    path('polizaUpdate/<str:pk>', login_required(PolizaUpdate.as_view()), name='poliza_update'),
    path('polizaDelete/<str:pk>', login_required(PolizaDelete.as_view()), name='poliza_delete'),
    path('getNameClient', Get_Name_Client, name='Name_client'),
    # -------------------------------------------------------->
    # Path Documentos
    path('documentoList', login_required(DocumentoList.as_view()), name='documento_list'),
    path('documentoCreate/<str:pk>', login_required(DocumentoCreate.as_view()), name='Documento_create')
]


