from django.contrib import admin
from produto.models import Produto, Venda

# Register your models here.

admin.site.register(Produto)
admin.site.register(Venda)