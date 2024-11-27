from django.db import models

# Create your models here.

class SalaModel(models.Model):

    numero = models.IntegerField()
    bloco = models.IntegerField()
    capacidade = models.IntegerField()
    tipo = models.CharField(max_length=20)
    disponivel = models.BooleanField()

    def __str__(self):
        return f'Sala {self.numero}'
    
    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"