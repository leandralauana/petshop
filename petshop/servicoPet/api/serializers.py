from rest_framework.serializers import ModelSerializer
from servicoPet.models import ServicoPet

class ServicoPetSerializer(ModelSerializer):
    
    class Meta:
        model = ServicoPet
        fields = "__all__"
        
    def validarHoario(self, data):
        conflitoHorario = ServicoPet.objects.filter(
            horarioEntrada__lt=data['horarioSaida'],
            horarioSaida__gt=data['horarioEntrada']
        )
        
        if conflitoHorario.exist():
            raise ServicoPetSerializer.ValidationError(
                "Já existe um serviço agendado neste horário"
            )
            
        return data     