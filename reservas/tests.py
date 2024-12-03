from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from reservas.models import SalaModel

# Create your tests here.

class SalaTesteCase(TestCase):

    def setUp(self):
        pass

    def test_cadastrar_sala(self):
        url = "http://localhost:8000/salas/"
        data = {
            "numero": 2,
            "bloco": 2,
            "capacidade": 30,
            "tipo": "Aula",
            "disponivel": True
        }
        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(SalaModel.objects.filter(numero=2,bloco=2).exists())

        response = self.client.post(url,data)
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
    
    def test_listar_salas(self):
        url = "http://localhost:8000/salas/"
        SalaModel.objects.create(
            numero=3,
            bloco=1,
            capacidade=30,
            tipo="Aula",
            disponivel=True
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['numero'],3)

