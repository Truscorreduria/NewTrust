from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.customer.models import PersonaNatural, PersonaJuridica
from django.db.models import CharField, Value, F
from django.db.models.functions import Concat
from apps.policy.forms import PolizaFrom, DocumentoForm
from apps.policy.models import Poliza, Documento
from django.http.response import JsonResponse


# ------------------------------------------------------------------------------------>
# view Poliza

class PolizaList(ListView):
    model = Poliza
    template_name = 'policy/policy_list.html'
    context_object_name = 'poliza_list'
    queryset = Poliza.objects.all()


class PolizaCreate(CreateView):
    model = Poliza
    form_class = PolizaFrom
    template_name = 'policy/policy_form.html'
    success_url = reverse_lazy('payment:recibo_create')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['poliza_id'] = self.object.pk
        return response

    def get_success_url(self):
        return reverse_lazy('payment:recibo_create', kwargs={'pk': self.object.pk})


class PolizaUpdate(UpdateView):
    model = Poliza
    form_class = PolizaFrom
    template_name = 'policy/policy_form.html'
    success_url = reverse_lazy('policy:poliza_list')


class PolizaDelete(DeleteView):
    model = Poliza
    form_class = PolizaFrom
    template_name = 'policy/policy_delete.html'
    success_url = reverse_lazy('policy:poliza_list')


# ------------------------------------------------------------------------------------>
# view Documento

class DocumentoList(ListView):
    model = Documento
    template_name = 'policy/documentacion/document_list.html'
    context_object_name = 'documento_list'
    queryset = Documento.objects.all()


class DocumentoCreate(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'policy/documentacion/document_form.html'
    success_url = reverse_lazy('payment:recibo_create')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['poliza_id'] = self.object.pk
        return response

    def get_success_url(self):
        return reverse_lazy('payment:recibo_create', kwargs={'pk': self.object.pk})

    def get_initial(self):
        idPoliza = self.kwargs["pk"]
        return {'poliza': idPoliza}

# ------------------------------------------------------------------------------------>
# view Lista Clientes Persona Natural y Juridica


def Get_Name_Client(request):
    q = request.GET.get('q')
    result = {'results': []}
    if q:
        PN = PersonaNatural.objects.annotate(
            text=Concat(
                'primerNombre', Value(' '), 'segundoNombre', Value(' '), 'primerApellido', Value(' '),
                'segundoApellido', output_field=CharField()
            )
        ).filter(text__icontains=q).values("id", "text")
        PJ = PersonaJuridica.objects.filter(nombre__icontains=q)\
            .annotate(id=F('ruc'), text=F('nombre')).values("id", "text")
        result['results'] = list(PJ) + list(PN)
    return JsonResponse(result, safe=False)







