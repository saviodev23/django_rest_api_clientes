# Django REST API - Consumindo API Pública de Cadastros de Usuários

Este é um projeto Django REST API desenvolvido para demonstrar como consumir uma API pública de cadastros de usuários. O objetivo principal é mostrar como integrar e utilizar dados de uma API externa em um projeto Django.

## Pré-requisitos

Certifique-se de ter o Python e o Django instalados em seu ambiente de desenvolvimento. Você pode instalar as dependências executando:

```bash
pip install -r requirements.txt
```

## Configuração

1. Clone o repositório:

```bash
git clone https://github.com/saviodev23/django_rest_api_clientes.git
cd django_rest_api_clientes
```

2. Execute as migrações do Django para configurar o banco de dados:

```bash
python manage.py migrate
```

## Uso

Para iniciar o servidor de desenvolvimento, execute o seguinte comando:

```bash
python manage.py runserver
```

Acesse a API em [http://localhost:8000/usuarios/](http://localhost:8000/api/usuarios/) para visualizar os dados dos usuários consumidos da API pública.

## Endpoint

- `/usuarios/`: Retorna a lista de usuários consumidos da API pública.


## imagem da página
![consumer_api](https://github.com/saviodev23/django_rest_api_clientes/assets/132952225/edb35de6-f403-4c50-80b1-98cdf030b2cc)



### Neste projeto também é possível fazer a criação da própria API do django. Isso é possivel utilizando o django rest framework.
Para fazer com que rode a própria API, retire os comentários do código nos arquivos views.py localizado no app "clientes" e urls.py que está na pasta "setup" do projeto.

### Imagens da página
![api_django1](https://github.com/saviodev23/django_rest_api_clientes/assets/132952225/a5e6fe82-2b98-4336-87b4-89e6d972d4d9)

![api_django2](https://github.com/saviodev23/django_rest_api_clientes/assets/132952225/cf8b8325-5441-4e92-a01e-6bf0b81286b9)

![api_django3](https://github.com/saviodev23/django_rest_api_clientes/assets/132952225/cd80e8d0-21ca-4c47-a9a5-d2ee601d25d0)
