from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.payment.views import ReciboCreate

app_name = 'payment'

urlpatterns = [
        path('createRecibo/<str:pk>', login_required(ReciboCreate.as_view()), name='recibo_create')
]