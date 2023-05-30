from rest_framework import viewsets
from rest_framework.response import Response
import requests


class CepView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        r = requests.get(f'https://brasilapi.com.br/api/cep/v1/{pk}')
        return Response(r.json())
