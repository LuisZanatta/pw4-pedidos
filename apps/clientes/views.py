from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


from .models import Cliente
from .forms import ClienteForm

class ClienteCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    tempalte_name = 'clientes/cliente_form.html'
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente adicionado com sucesso!'
    success_url = reverse_lazy('pedidos__home')


class ClienteUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    tempalte_name = 'clientes/cliente_form.html'
    model = Cliente
    form_class = ClienteForm
    success_message = 'Cliente atualizado com sucesso!'