from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    quantidadeEstoque = models.PositiveIntegerField()
    
    def __str__(self):
        return f'Produto {self.nome}'
    
    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    dataVenda = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):        
        
        if self.produto.quantidadeEstoque < self.quantidade:
            raise ValueError("Produto não se encontra no estoque")
        
        self.produto.quantidadeEstoque -= self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)