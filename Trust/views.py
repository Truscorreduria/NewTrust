from django.views.generic import TemplateView


# --------------------------------------------------------
# Dashboard

class IndexView(TemplateView):
    template_name = "dashboard/index.html"
