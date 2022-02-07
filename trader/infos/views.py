from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import pandas as pd

class Information(APIView):
    def get(papel, url):
        consolidado_acoes = pd.DataFrame()
        acoesTodas = pd.read_excel("IBOV.xlsx")
        for codigo_acao in acoesTodas["Código"]:
            url = "https://www.fundamentus.com.br/detalhes.php?papel="+ codigo_acao
            headers = {
                 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            page = requests.get(url, headers=headers)
            acao = pd.read_html(page.text, decimal=",", thousands=".")

            acao[0] = acao[0].transpose()
            acao[1] = acao[1].transpose()
            info_1 = acao[0].iloc[:2, :]
            info_2 = acao[0].iloc[2:, :]
            info_3 = acao[1].iloc[:2, :]
            info_4 = acao[1].iloc[2:, :]
            info_2 = info_2.reset_index(drop=True)
            info_4 = info_4.reset_index(drop=True)
            acao = pd.concat([info_1, info_2, info_3, info_4], axis=1, join="inner")
            acao.columns = acao.iloc[0]
            colunaTratada = [coluna.replace("?", "") for coluna in acao.columns]
            acao.columns = colunaTratada
            acao = acao.drop(0)
            consolidado_acoes = consolidado_acoes.append(acao, sort=False)
        return Response(consolidado_acoes)
        
