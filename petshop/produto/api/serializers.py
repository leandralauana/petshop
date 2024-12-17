from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from produto.models import Produto, Venda

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'quantidadeEstoque']
        
class VendaSerializer(serializers.ModelSerializer):
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = Venda
        fields = ['id', 'produto', 'quantidade', 'dataVenda']

    def validate(self, data):
        produto = data['produto']
        quantidade = data['quantidade']

        if produto.quantidadeEstoque < quantidade:
            raise serializers.ValidationError("Estoque insuficiente para essa venda.")
        return data        