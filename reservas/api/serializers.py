from rest_framework.serializers import ModelSerializer

from reservas.models import SalaModel

class SalaSerializer(ModelSerializer):

    class Meta:
        model = SalaModel
        fields = "__all__"
