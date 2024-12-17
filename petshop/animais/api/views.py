from typing import Any
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from animais.api.serializers import AnimalSerializer
from animais.models import Animal

class AnimalViewSet(ModelViewSet):
    serializer_class = AnimalSerializer
    permission_classes = [AllowAny]
    queryset = Animal.objects.all()