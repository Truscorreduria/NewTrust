from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.payment.forms import ReciboFrom
from apps.payment.models import Recibo
from apps.policy.models import Poliza


# ------------------------------------------------------------------------------------>
# view forma de pago


class ReciboCreate(CreateView):
    Model = Recibo
    form_class = ReciboFrom
    template_name = 'payment/formaDePago_form.html'
    success_url = reverse_lazy('policy:PolizaDocumento_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        idPoliza = self.kwargs["pk"]
        ramo = Poliza.objects.filter(id=idPoliza).values('ramo__Nombre')
        subRamo = Poliza.objects.filter(id=idPoliza).values('subramo__Nombre')
        aseguradora = Poliza.objects.filter(id=idPoliza).values('aseguradora__Nombre')
        fInicioVigencia = Poliza.objects.filter(id=idPoliza).values('fechaInicio')
        fFinVigencia = Poliza.objects.filter(id=idPoliza).values('fechaFin')
        cliente = Poliza.objects.filter(id=idPoliza).values('cliente')
        grupo = Poliza.objects.filter(id=idPoliza).values('grupo__Nombre')
        context['poliza'] = idPoliza
        context['ramo'] = ramo[0]['ramo__Nombre']
        context['subRamo'] = subRamo[0]['subramo__Nombre']
        context['aseguradora'] = aseguradora[0]['aseguradora__Nombre']
        context['fInicioVigencia'] = fInicioVigencia[0]['fechaInicio']
        context['fFinVigencia'] = fFinVigencia[0]['fechaFin']
        context['cliente'] = cliente[0]['cliente']
        context['grupo'] = grupo[0]['grupo__Nombre']
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['poliza_id'] = self.object.poliza_id
        return response

    def get_success_url(self):
        poliza_id = self.object.poliza_id
        if poliza_id:
            return reverse_lazy('policy:PolizaDocumento_create', kwargs={'pk': poliza_id})
        return reverse_lazy('policy:poliza_create')

    def get_initial(self):
        idPoliza = self.kwargs["pk"]
        return {'poliza': idPoliza}


