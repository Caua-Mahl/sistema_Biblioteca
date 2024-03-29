from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'home.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cadastrar(request):
    novoUsuario = Usuario()
    novoUsuario.nome  = request.POST['nome']
    novoUsuario.email = request.POST['email']
    if request.POST['senha'] == request.POST['confirmarSenha']:
        novoUsuario.senha = request.POST['senha']
        novoUsuario.save()
        return render(request, 'cadastro.html', {'sucesso': 'Usuário cadastrado com sucesso!'})
    
    return render(request, 'cadastro.html', {'erro': 'Senhas não conferem!'})