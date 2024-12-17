from rest_framework.serializers import ModelSerializer
from animais.models import Animal

class AnimalSerializer(ModelSerializer):
    
    class Meta:
        model = Animal
        fields = "__all__"