from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Cotacao, DadosEmpresa

class DadosEmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DadosEmpresa
        fields = (
            "id",
            "papel",
            "tipo",
            "empresa",
            "setor",
            "subsetor",
            "cotacao",
            "volumeMedio",
            "valorMercado",
            "valorFirma",
            "ultimoBalanco",
            "numeroDeAcoes",
        )
class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
        fields = (
           "data",
           "cotacao", 
        )