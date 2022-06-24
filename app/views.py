from django.shortcuts import render, redirect
from app.models import Postagem, Cliente
from django.contrib import messages


def pagina(request):
    return render(request, "base/pagina.html")

def postagem(request):
    postagemLista = Postagem.objects.all()
    return render(request, "base/postagem.html", {"postagens": postagemLista})

def lista(request):
    clienteLista = Cliente.objects.all()
    return render(request, "base/lista.html", {"clientes": clienteLista})

def add(request):
    if request.method == "POST":
        nome = request.POST['nome']
        cpf = request.POST['cpf']
        telefone = request.POST['telefone']
        cliente = Cliente.objects.create(nome=nome, cpf=cpf, telefone=telefone)
        messages.info(request, "Cliente adicionado com sucesso!")
    else:
        messages.info(request, "Erro ao adicionar: Cliente já existe!")
    return redirect('/app/lista')

def edit(request, id):
    cliente = Cliente.objects.get(pk=id)
    clienteLista = Cliente.objects.all()
    context = {
        'cliente': cliente,
        'clienteLista': clienteLista
    }
    return render(request, "base/lista.html", context)

def edit_id(request, id):
    pessoa = Cliente.objects.get(pk=id)
    pessoa.nome = request.POST['nome']
    pessoa.cpf = request.POST['cpf']
    pessoa.telefone = request.POST['telefone']
    pessoa.save()
    messages.info(request, "Cliente atualizado com sucesso!")
    return redirect('/app/lista')

def delete(request, id):
    cliente = Cliente.objects.get(pk=id)
    cliente.delete()
    messages.info(request, "Cliente delete com sucesso!")
    return redirect('/app/lista')
