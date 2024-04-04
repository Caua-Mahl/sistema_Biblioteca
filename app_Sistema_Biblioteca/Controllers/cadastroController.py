from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_Sistema_Biblioteca.Models.Usuario import Usuario

def cadastro(request):
    return render(request, 'cadastro.html')

def cadastrar(request):
    novoUsuario = Usuario()
    novoUsuario.nome  = request.POST['nome']
    novoUsuario.email = request.POST['email']
    novoUsuario.senha = request.POST['senha']

    try :
        novoUsuario.validarDadosCadastro(request.POST['confirmarSenha'])

        if novoUsuario.nome[0] == ' ':
            novoUsuario.nome = novoUsuario.nome[1:]

        User.objects.create_user(username=novoUsuario.email, email=novoUsuario.email, password=novoUsuario.senha)
        novoUsuario.save()
        
        return render(request, 'login.html', {'sucesso': 'Usuário cadastrado com sucesso!'})

    except Exception as e:
        return render(request, 'cadastro.html', {'erro': e})
    