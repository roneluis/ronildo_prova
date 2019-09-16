from django.shortcuts import render


def home (request):
    return render(request, 'home.html')

def produto_list (request):
    produtos = Produto.objects.all()
    return render(request, 'produto/list.html', {'produtos':produtos})

def produto_show(request):
    produtos = Produto.objects.all()
    return render(request, 'produto/show.html', {'produtos':produtos})

def produto_form (request):
    if (request.method == 'POST'):
        form = ProdutoForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect ('/produto/produto/')
        else:
            return render(request, 'produto/form.html', {'form':form})  
    else:
        form = ProdutoForm()
        return render(request, 'produto/form.html', {'form':form})

def produto_edit (request, produto_id):
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
