from typing import Any
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from servicoPet.api.serializers import ServicoPetSerializer
from servicoPet.models import ServicoPet

class ServicoPetViewSet(ModelViewSet):
    serializer_class = ServicoPetSerializer
    permission_classes = [AllowAny]
    queryset = ServicoPet.objects.all()
    