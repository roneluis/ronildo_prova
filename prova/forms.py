from django.urls import path
from . models import Produto

class ProdutoForm():
    class Meta:
        model = Produto
        fields= '__all__'