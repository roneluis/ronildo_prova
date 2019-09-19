from django.shortcuts import render
from . models import Produto
from . forms import ProdutoForm


def home (request):
    return render(request, 'home.html')

def produto_list (request):
    produtos = Produto.objects.all()
    return render(request, 'list.html/', {'produtos':produtos})

def produto_show(request):
    produtos = Produto.objects.all()
    return render(request, 'show.html/', {'produtos':produtos})


def produto_form (request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect ('/produto/produto/')
        else:
            return render(request, 'form.html/', {'form':form})  
    else:
        form = ProdutoForm()
        return render(request, 'form.html/', {'form':form})

def produto_excluir(request, produto_id):
          aluno=Aluno.objects.get(pk=aluno_id)
          aluno.delete()
          return redirect ('/prova/produto/')


def produto_editar (request, produto_id):
     if (request.method == 'POST'):
        produto=Produto.objects.get(pk=produto_id)
        form = ProdutoForm(request.POST, instance = produto)
        if form.is_valid():
             form.save()
             return redirect ('/prova/produto/')
        else: 
             return render (request, 'produto/edit.html', {'form':form, 'produto_id': produto_id})
    
     else:
         produto=Produto.objects.get(pk=produto_id)    
         form = ProdutoForm(instance = produto)
         return render (request, 'produto/edit.html', {'form':form, 'produto_id': produto_id})
 

# Create your views here.
