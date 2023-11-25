from django.shortcuts import render
from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend

#consumindo API
import requests

# class ClientesViewSet(viewsets.ModelViewSet):
#     """Listando clientes"""
#     queryset = Cliente.objects.all()
#     serializer_class = ClienteSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]#faz com que seja possivel fazer o filtro dos clientes
#     ordering_fields = ['nome']#filtrando os clientes por nome
#     search_fields = ['nome', 'cpf']#possibilita fazer a busca por nome e cpf do cliente
#     filterset_fields = ['ativo']#busca exata, verdadeiro ou falso
#
#

def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    context = {
        'users': users
    }
    return render(request, 'index.html', context)
