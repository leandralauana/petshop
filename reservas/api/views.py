from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from reservas.api.serializers import SalaSerializer
from reservas.models import SalaModel

class SalaViewSet(ModelViewSet):
    serializer_class = SalaSerializer
    permission_classes = [AllowAny]
    queryset = SalaModel.objects.all()
    