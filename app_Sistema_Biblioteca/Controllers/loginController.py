from django.shortcuts import render
from django.contrib.auth import authenticate, login
from app_Sistema_Biblioteca.Models.Usuario import Usuario
from app_Sistema_Biblioteca.Models.Livros  import Livros
import hashlib  

def login(request):
    if 'usuario' in request.session:
        return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})
    
    return render(request, 'login.html')

def logar(request):
    usuario = Usuario()
    usuario.email = request.POST['email']
    usuario.senha = request.POST['senha']

    try:
        usuario.validarDadosLogin()

        login = authenticate(request, username=request.POST['email'], password=hashlib.md5(request.POST['senha'].encode()).hexdigest())

        if login is None:
            raise Exception('Email ou senha inválidos!')
        
        usuario = Usuario.objects.get(email=request.POST['email'])
        request.session['usuario'] = {'id': usuario.id, 'nome': usuario.nome}

        request.session['usuario']['admin'] = True if usuario.admin == True else False

        if 'lembrar' in request.POST:
            request.session.set_expiry(0)
        
        return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})
    
    except Exception as e:
        return render(request, 'login.html', {'erro': e})

def logout(request):
    if 'usuario' not in request.session:
        return render(request, 'login.html')

    if 'usuario' in request.session:
        del request.session['usuario']
    
    return render(request, 'login.html', {'sucesso': 'Usuário deslogado com sucesso!'})