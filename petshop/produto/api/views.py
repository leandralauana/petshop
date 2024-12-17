from typing import Any
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from produto.api.serializers import ProdutoSerializer, VendaSerializer
from produto.models import Produto, Venda

class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    permission_classes = [AllowAny]
    queryset = Produto.objects.all()
    
class VendaViewSet(ModelViewSet):
    serializer_class = VendaSerializer
    permission_classes = [AllowAny]
    queryset = Venda.objects.all()  