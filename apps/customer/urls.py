from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.customer.views import PersonaNaturalList, PersonaNaturalCreate, PersonaJuridicaList, PersonaJuridicaCreate, \
    PersonaNaturalUpdate, PersonaNaturalDelete, PersonaJuridicaUpdate, PersonaJuridicaDelete, EmpresaList, \
    EmpresaCreate, EmpresaDelete

app_name = 'customer'

urlpatterns = [
    # -------------------------------------------------------->
    # Path Persona Natural
    path('personaNaturalList', login_required(PersonaNaturalList.as_view()), name='personaNatural_list'),
    path('personaNaturalCreate', login_required(PersonaNaturalCreate.as_view()), name='personaNatural_create'),
    path('personaNaturalU/<str:pk>', login_required(PersonaNaturalUpdate.as_view()), name='personaNatural_update'),
    path('personaNaturalD/<str:pk>', login_required(PersonaNaturalDelete.as_view()), name='personaNatural_delete'),
    # -------------------------------------------------------->
    # Path Persona Juridica
    path('personaJuridicaList', login_required(PersonaJuridicaList.as_view()), name='personaJuridica_list'),
    path('personaJuridicaCreate', login_required(PersonaJuridicaCreate.as_view()), name='personaJuridica_create'),
    path('personaJuridicaU/<str:pk>', login_required(PersonaJuridicaUpdate.as_view()), name='personaJuridica_update'),
    path('personaJuridicaD/<str:pk>', login_required(PersonaJuridicaDelete.as_view()), name='personaJuridica_delete'),
    # -------------------------------------------------------->
    # Path Empresa
    path('empresaList', EmpresaList.as_view(), name='empresa_list'),
    path('empresaCreate', EmpresaCreate.as_view(), name='empresa_create'),
    path('empresaDelete/<str:pk>', login_required(EmpresaDelete.as_view()), name='empresa_delete'),

]
