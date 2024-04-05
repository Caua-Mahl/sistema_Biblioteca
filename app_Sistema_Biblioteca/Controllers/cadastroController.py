from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_Sistema_Biblioteca.Models.Usuario import Usuario

def cadastro(request):
    if 'usuario' in request.session:
        return render(request, 'home.html', { 'erro' : 'Você já está logado!' })
        
    return render(request, 'cadastro.html')

def cadastrar(request):
    if 'usuario' in request.session:
        return render(request, 'home.html')

    novoUsuario = Usuario()
    novoUsuario.nome  = request.POST['nome']
    novoUsuario.email = request.POST['email']
    novoUsuario.senha = request.POST['senha']

    try :
        novoUsuario.validarDadosCadastro(request.POST['confirmarSenha'])

        if novoUsuario.nome[0] == ' ':
            novoUsuario.nome = novoUsuario.nome[1:]

        if novoUsuario.nome[-1] == ' ':
            novoUsuario.nome = novoUsuario.nome[:-1]

        if novoUsuario.email == 'admin@gmail.com':
            novoUsuario.admin = True

        User.objects.create_user(username=novoUsuario.email, email=novoUsuario.email, password=novoUsuario.senha)
        novoUsuario.save()
        
        return render(request, 'login.html', {'sucesso': 'Usuário cadastrado com sucesso!'})

    except Exception as e:
        return render(request, 'cadastro.html', {'erro': e})
    