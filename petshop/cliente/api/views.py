from typing import Any
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from cliente.api.serializers import ClienteSerializer
from cliente.models import Cliente

class ClienteViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]
    queryset = Cliente.objects.all()