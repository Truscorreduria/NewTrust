
from django.urls import path
from apps.home.views import HomeView, WeView, BusinessLineView, InsuranceView, PlatformsView, ContactView

app_name = 'home'

urlpatterns = [
    # -------------------------------------------------------->
    # Path Home
    path('', HomeView.as_view(), name='index'),
    path('nosotros/', WeView.as_view(), name='nosotros'),
    path('lineas/', BusinessLineView.as_view(), name='lineas'),
    path('corredor/', InsuranceView.as_view(), name='corredor'),
    path('plataformas/', PlatformsView.as_view(), name='plataformas'),
    path('contacto/', ContactView.as_view(), name='contacto'),
]
