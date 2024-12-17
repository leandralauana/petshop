from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()
    
    def __str__(self):
        return f'Cliente {self.nome}'
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"