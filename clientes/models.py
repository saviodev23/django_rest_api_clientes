from django.db import models

#Este model faz com que seja gerado a tabela Cliente no BD
# para que a API do django faça os registros através do formulário
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=9)
    celular = models.CharField(max_length=14)
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome
