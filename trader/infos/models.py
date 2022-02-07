from pyexpat import model
from django.db import models


class Cotacao(models.Model):
    data = models.DateField(auto_now=True)
    cotacao = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id


class DadosEmpresa(models.Model):
    papel = models.CharField(max_length=100)
    tipo = models.CharField(max_length=4)
    empresa = models.CharField(max_length=100)
    setor = models.CharField(max_length=150)
    subsetor = models.CharField(max_length=150)
    cotacao = models.ForeignKey(Cotacao, related_name="cotacaoEmpresa", on_delete=models.CASCADE)
    volumeMedio = models.DecimalField(max_digits=90, decimal_places=2)
    valorMercado = models.DecimalField(max_digits=900, decimal_places=2)
    valorFirma = models.DecimalField(max_digits=900, decimal_places=2)
    ultimoBalanco = models.DateField()
    numeroDeAcoes = models.DecimalField(max_digits=90, decimal_places=0)

    def __str__(self):
        return '%s' % self.id
