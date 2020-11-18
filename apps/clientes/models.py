from django.db import models

class Cliente(models.Model):

    nome = models.CharField(max_length=254, verbose_name="Nome")
    endereco = models.CharField(max_length=254, verbose_name="Endereço")
    numero = models.CharField(max_length=10, verbose_name="Número")
    complemento = models.CharField(max_length=50, blank=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    cidade = models.CharField(max_length=254, verbose_name="Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    telefone = models.CharField(max_length=19, blank=True, verbose_name="Telefone Fixo")
    celular = models.CharField(max_length=19, blank=True, verbose_name="Celular")
    rg = models.CharField(max_length=15, verbose_name="RG")
    cpf = models.CharField(max_length=15, verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(max_length=254, verbose_name="Email")
  
    class Meta:
        verbose_name = 'Cliente '
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome