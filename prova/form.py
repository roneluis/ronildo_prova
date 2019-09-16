from django.urls import path

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields= '__all__'