from django.views.generic import TemplateView


# --------------------------------------------------------
# Home
class HomeView(TemplateView):
    template_name = "home/index.html"


class WeView(TemplateView):
    template_name = "home/nosotros.html"


class BusinessLineView(TemplateView):
    template_name = "home/lineas.html"


class InsuranceView(TemplateView):
    template_name = "home/corredor.html"


class PlatformsView(TemplateView):
    template_name = "home/plataformas.html"


class ContactView(TemplateView):
    template_name = "home/contacto.html"



