from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_Sistema_Biblioteca.Models.Usuario import Usuario
from app_Sistema_Biblioteca.Models.Livros import Livros


def home(request):
    return render(request, 'home.html')

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
        
        return render(request, 'cadastro.html', {'sucesso': 'Usuário cadastrado com sucesso!'})

    except Exception as e:
        return render(request, 'cadastro.html', {'erro': e})
    

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
        
        request.session['usuario'] = {
            'nome' : usuario.nome,
            'email': usuario.email
        }

        return render(request, 'home.html', {'sucesso':  usuario.nome + ' logado com sucesso!'})
    
    except Exception as e:
        return render(request, 'login.html', {'erro': e})

def logout(request):
    if 'usuario' in request.session:
        del request.session['usuario']
    
    return render(request, 'home.html', {'sucesso': 'Usuário deslogado com sucesso!'})

def livros(request):
    return render(request, 'livros.html', {'livros': Livros.objects.all()})



def cadastrarLivro(request):

    if request.method == 'GET':
        return render(request, 'cadastrarLivro.html')
    
    if not all([request.POST['titulo'], request.POST['autor'], request.POST['genero'], request.POST['lancamento']]):
        return render(request, 'cadastrarLivro.html', {'erro': 'Preencha todos os campos!'})
    
    novoLivro            = Livros()
    novoLivro.titulo     = request.POST['titulo'] 
    novoLivro.autor      = request.POST['autor']
    novoLivro.genero     = request.POST['genero']
    novoLivro.lancamento = request.POST['lancamento']
    novoLivro.notaMedia  = 0.0

    try:
        novoLivro.validarDados()
        novoLivro.save()
        return render(request, 'cadastrarLivro.html', {'sucesso': 'Livro cadastrado com sucesso!'})
    except Exception as e:
        return render(request, 'cadastrarLivro.html', {'erro': e})
