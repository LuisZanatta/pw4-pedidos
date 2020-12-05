from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class PedidosHome(LoginRequiredMixin, TemplateView):
    template_name = "pedidos/pedidos.html"