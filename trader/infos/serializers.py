from dataclasses import fields
from rest_framework import serializers

from .models import DadosEmpresa

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