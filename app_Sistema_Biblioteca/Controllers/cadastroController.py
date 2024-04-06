from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_Sistema_Biblioteca.Models.Usuario import Usuario
from app_Sistema_Biblioteca.Models.Livros  import Livros

def cadastro(request):
    if 'usuario' in request.session:
        return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})
        
    return render(request, 'cadastro.html')

def cadastrar(request):
    if 'usuario' in request.session and request.session['usuario']['admin'] == False:
            return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})

    novoUsuario       = Usuario()
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

        if request.session['usuario']['admin'] == True:
           return render(request, 'adminLivro.html', {'sucesso': 'Usuário cadastrado com sucesso!', 'livros': Livros.objects.all()})
                                           
        return render(request, 'login.html', {'sucesso': 'Usuário cadastrado com sucesso!'})

    except Exception as e:
        if request.session['usuario']['admin'] == True:
            return render(request, 'adminLivro.html', {'erro': e, 'livros': Livros.objects.all()})

        return render(request, 'cadastro.html', {'erro': e})
    