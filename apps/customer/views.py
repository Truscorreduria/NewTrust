from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.customer.models import PersonaNatural, PersonaJuridica, Empresa
from apps.customer.forms import PersonaNaturalFrom, PersonaJuridicaFrom, EmpresaFrom


# ------------------------------------------------------------------------------------>
# view Personal Natural


class PersonaNaturalList(ListView):
    model = PersonaNatural
    template_name = 'customer/personaNatural/customer_list.html'
    context_object_name = 'personaNatural_list'
    queryset = PersonaNatural.objects.all()


class PersonaNaturalCreate(CreateView):
    model = PersonaNatural
    form_class = PersonaNaturalFrom
    template_name = 'customer/personaNatural/customer_form.html'
    success_url = reverse_lazy('customer:personaNatural_list')


class PersonaNaturalUpdate(UpdateView):
    model = PersonaNatural
    form_class = PersonaNaturalFrom
    template_name = 'customer/personaNatural/customer_form.html'
    success_url = reverse_lazy('customer:personaNatural_list')


class PersonaNaturalDelete(DeleteView):
    model = PersonaNatural
    template_name = 'customer/personaNatural/customer_delete.html'
    success_url = reverse_lazy('customer:personaNatural_list')

# ------------------------------------------------------------------------------------>
# view Personal Juridica


class PersonaJuridicaList(ListView):
    model = PersonaJuridica
    template_name = 'customer/personaJuridica/customer_list.html'
    context_object_name = 'personaJuridica_list'
    queryset = PersonaJuridica.objects.all()


class PersonaJuridicaCreate(CreateView):
    model = PersonaJuridica
    form_class = PersonaJuridicaFrom
    template_name = 'customer/personaJuridica/customer_form.html'
    success_url = reverse_lazy('customer:personaJuridica_list')


class PersonaJuridicaUpdate(UpdateView):
    model = PersonaJuridica
    form_class = PersonaJuridicaFrom
    template_name = 'customer/personaJuridica/customer_form.html'
    success_url = reverse_lazy('customer:personaJuridica_list')


class PersonaJuridicaDelete(DeleteView):
    model = PersonaJuridica
    template_name = 'customer/personaJuridica/customer_delete.html'
    success_url = reverse_lazy('customer:personaJuridica_list')

# ------------------------------------------------------------------------------------>
# view Empresa


class EmpresaList(ListView):
    model = Empresa
    template_name = 'customer/empresa/empresa_list.html'
    context_object_name = 'empresa_list'
    queryset = Empresa.objects.all()


class EmpresaCreate(CreateView):
    model = Empresa
    form_class = EmpresaFrom
    template_name = 'customer/empresa/empresa_form.html'
    success_url = reverse_lazy('customer:empresa_list')


class EmpresaDelete(DeleteView):
    model = Empresa
    template_name = 'customer/empresa/empresa_delete.html'
    success_url = reverse_lazy('customer:empresa_list')


