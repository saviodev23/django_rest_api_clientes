from django.contrib import admin
from django.urls import path, include
# from rest_framework import routers
# from clientes.views import ClientesViewSet

# router = routers.DefaultRouter()
# router.register('clientes', ClientesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('clientes.urls')),
    # path('', include(router.urls)),
]

#Para rodar a API própria, decomente os imports e o path