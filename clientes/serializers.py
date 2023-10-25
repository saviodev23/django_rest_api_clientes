from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido!"})   
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua números neste campo."})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 digitos."})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir esse padrão: 77 91234-1234."})
        return data
    
    #A função sempre deve começar com "validade_"
    # def valida_cpf(self, cpf):
    #     if not len(cpf) != 11:
    #         raise serializers.ValidationError('CPF deve conter pelo menos 11 digitos')