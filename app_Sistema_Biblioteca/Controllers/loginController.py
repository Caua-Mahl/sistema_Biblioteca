from django.shortcuts import render
from django.contrib.auth import authenticate, login
from app_Sistema_Biblioteca.Models.Usuario import Usuario

def login(request):
    if 'usuario' in request.session:
        return render(request, 'home.html')
    
    return render(request, 'login.html')

def logar(request):
    usuario = Usuario()
    usuario.email = request.POST['email']
    usuario.senha = request.POST['senha']

    try:
        usuario.validarDadosLogin()

        login = authenticate(request, username=request.POST['email'], password=request.POST['senha'])

        if login is None:
            raise Exception('Email ou senha inválidos!')
        
        usuario = Usuario.objects.get(email=request.POST['email'])
        request.session['usuario'] = {'id': usuario.id, 'nome': usuario.nome}


        return render(request, 'home.html', {'sucesso':  request.session['usuario']['nome'] + ' logado com sucesso!'})
    
    except Exception as e:
        return render(request, 'login.html', {'erro': e})

def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return render(request, 'home.html', {'sucesso': 'Usuário deslogado com sucesso!'})