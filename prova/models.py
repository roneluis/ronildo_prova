from django.db import models

class Carrinho_De_Compras (models.Model):
     tamanho= models.CharField(max_length = 50)
     peso= models.CharField(max_length=20)

class Produto (models.Model):
     marca= models.CharField(max_length = 50)
     nome= models.CharField(max_length=20)
     carrinho_De_Compras= models.ForeignKey(Carrinho_De_Compras,on_delete=models.CASCADE)

class Cliente (models.Model):
    nome= models.CharField(max_length = 50)
    idade= models.CharField(max_length=20)
    produto= models.ForeignKey(Produto,on_delete=models.CASCADE)



# Create your models here.
