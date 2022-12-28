from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View, DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.contrib.auth.mixins import LoginRequiredMixin


from apps.certificacion.models import *

##Asesorador

class AsesoradorListView(LoginRequiredMixin,ListView):
    model = Asesorador
    fields = ('__all__')
    success_url = reverse_lazy('asesorador_list')
    template_name = 'certificacion/asesorador_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_asesorador'
        return context

class AsesoradorCreateView(LoginRequiredMixin, CreateView):
    model = Asesorador
    fields = ('__all__')
    success_url = reverse_lazy('asesorador_list')
    template_name = 'certificacion/asesorador_create.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_asesorador'
        return context


class AsesoradorUpdateView(LoginRequiredMixin,UpdateView):
    model = Asesorador
    fields = ('__all__')
    success_url = reverse_lazy('asesorador_list')
    template_name = 'certificacion/Asesorador_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_asesorador'
        return context


class AsesoradorDeleteView(LoginRequiredMixin,DeleteView):
    model = Asesorador
    fields = ('__all__')
    success_url = reverse_lazy('asesorador_list')
    template_name = 'certificacion/asesorador_delete.html'



##Certificador
class CertificadorListView(LoginRequiredMixin,ListView):
    model = Certificador
    fields = ('__all__')
    success_url = reverse_lazy('certificador_list')
    template_name = 'certificacion/certificador_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-certificadores'
        return context


class CertificadorCreateView(LoginRequiredMixin, CreateView):
    model = Certificador
    fields = ('__all__')
    success_url = reverse_lazy('certificador_list')
    template_name = 'certificacion/certificador_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-certificadores'
        return context


class CertificadorUpdateView(LoginRequiredMixin,UpdateView):
    model = Certificador
    fields = ('__all__')
    success_url = reverse_lazy('certificador_list')
    template_name = 'certificacion/certificador_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'general-settings-certificadores'
        return context


class CertificadorDeleteView(LoginRequiredMixin,DeleteView):
    model = Certificador
    fields = ('__all__')
    success_url = reverse_lazy('certificador_list')
    template_name = 'certificacion/certificador_delete.html'


##Cliente

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    fields = ('__all__')
    success_url = reverse_lazy('cliente_list')
    template_name = 'certificacion/cliente_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_cliente'
        return context

class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ('__all__')
    success_url = reverse_lazy('cliente_list')
    template_name = 'certificacion/cliente_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_cliente'
        return context


class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    fields = ('name','organismo')
    success_url = reverse_lazy('cliente_list')
    template_name = 'certificacion/cliente_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_cliente'
        return context



class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    model = Cliente
    fields = ('__all__')
    success_url = reverse_lazy('cliente_list')
    template_name = 'certificacion/cliente_delete.html'


##Psi

class PsiListView(LoginRequiredMixin,ListView):
    model = PSI
    fields = ('__all__')
   
    success_url = reverse_lazy('psi_list')
    template_name = 'certificacion/psi_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_psi'
        return context


class PsiCreateView(LoginRequiredMixin, CreateView):
    model = PSI
    fields = ('fecha','cliente','asesorador','dictaminador','certificador')
    success_url = reverse_lazy('psi_list')
    template_name = 'certificacion/psi_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_psi'
        return context

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()

        cant = Certifico.objects.all().count() + 1
        certifico =  Certifico.objects.create(code=f'{cant}-DPSI-{self.object.fecha.month}-{self.object.fecha.year}',fecha=self.object.fecha,  psi= self.object)
        certifico.save()
        return super().form_valid(form)

class PsiUpdateView(LoginRequiredMixin,UpdateView):
    model = PSI
    fields = ('fecha','cliente','asesorador','certificador')
    success_url = reverse_lazy('psi_list')
    template_name = 'certificacion/psi_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_psi'
        return context

    

class PsiDeleteView(LoginRequiredMixin,DeleteView):
    model = PSI
    fields = ('__all__')
    success_url = reverse_lazy('psi_list')
    template_name = 'certificacion/psi_delete.html'





##Certifico

class CertificoListView(LoginRequiredMixin,ListView):
    model = Certifico
    fields = ('__all__')
    success_url = reverse_lazy('certifico_list')
    template_name = 'certificacion/certifico_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_certifico'
        return context

class CertificoPendienteListView(LoginRequiredMixin,ListView):
    model = Certifico
    fields = ('__all__')
    success_url = reverse_lazy('certifico_list_pen')
    template_name = 'certificacion/certifico_list_pen.html'
    def get_queryset(self, *args, **kwargs):
        query = self.model.objects.filter(estado = False)
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_cer_pen'
        return context

class CertificoCreateView(LoginRequiredMixin, CreateView):
    model = Certifico
    fields = ('__all__')
    success_url = reverse_lazy('certifico_list')
    template_name = 'certificacion/certifico_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_certifico'
        return context


class CertificoUpdateView(LoginRequiredMixin,UpdateView):
    model = Certifico
    fields = ('fecha','psi')
    success_url = reverse_lazy('certifico_list')
    template_name = 'certificacion/certifico_update.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_certifico'
        return context

class CertificoDetailView(LoginRequiredMixin,DetailView):
    model = Certifico
    fields = ('__all__')
    template_name = 'certificacion/certifico_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["segment"] = 'gestionar_certifico'
        return context

class CertificoDeleteView(LoginRequiredMixin,DeleteView):
    model = Certifico
    fields = ('__all__')
    success_url = reverse_lazy('certifico_list')
    template_name = 'certificacion/certifico_delete.html'


