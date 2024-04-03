from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from app_Sistema_Biblioteca.Models.Usuario import Usuario
from app_Sistema_Biblioteca.Models.Livros import Livros
from app_Sistema_Biblioteca.Models.Avaliacao import Avaliacao
from app_Sistema_Biblioteca.Models.Resenha import Resenha


def home(request):
    return render(request, 'home.html')

#_________________________________________________________________________________________________________


#Cadastro
#_________________________________________________________________________________________________________
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
    
#_________________________________________________________________________________________________________


#Login
#_________________________________________________________________________________________________________

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



#_________________________________________________________________________________________________________


#Livros
#_________________________________________________________________________________________________________

def livros(request):
    return render(request, 'livros.html', {'livros': Livros.objects.all()})

def adminLivro(request):

    if request.method == 'GET':
        return render(request, 'adminLivro.html', {'livros': Livros.objects.all()})
    
    try: 

        if not all([request.POST['titulo'], request.POST['autor'], request.POST['genero'], request.POST['lancamento']]):
            raise Exception('Preencha todos os campos!')
        
        novoLivro            = Livros()
        novoLivro.titulo     = request.POST['titulo'] 
        novoLivro.autor      = request.POST['autor']
        novoLivro.genero     = request.POST['genero']
        novoLivro.lancamento = request.POST['lancamento']
        novoLivro.notaMedia  = 0.0

        novoLivro.validarDados()

        if Livros.objects.filter(titulo=novoLivro.titulo, autor=novoLivro.autor):
            raise Exception('Livro já cadastrado!')
        
        novoLivro.save()
        return render(request, 'adminLivro.html', {'sucesso': 'Livro cadastrado com sucesso!', 'livros': Livros.objects.all()})
    except Exception as e:
        return render(request, 'adminLivro.html', {'erro': e, 'livros': Livros.objects.all()})
    
def editarLivro(request):
    try:
        
        if not all([request.POST['titulo'], request.POST['autor'], request.POST['genero'], request.POST['lancamento']]):
            raise Exception('Preencha todos os campos!')
        
        livro            = Livros.objects.get(id=request.POST['id'])
        livro.titulo     = request.POST['titulo']
        livro.autor      = request.POST['autor']
        livro.genero     = request.POST['genero']
        livro.lancamento = request.POST['lancamento']

        livro.validarDados()
        
        livro.save()
        return render(request, 'adminLivro.html', {'sucesso': 'Livro editado com sucesso!', 'livros': Livros.objects.all()})
    
    except Exception as e:
        return render(request, 'adminLivro.html', {'erro': e, 'livros': Livros.objects.all()})
    
def excluirLivro(request):
    try:
        livro = Livros.objects.get(id=request.POST['id'])
        livro.delete()
        return render(request, 'adminLivro.html', {'sucesso': 'Livro excluído com sucesso!', 'livros': Livros.objects.all()})
    except Exception as e:
        return render(request, 'adminLivro.html', {'erro': 'Não foi possivel excluir o livro', 'livros': Livros.objects.all()})
    
#_________________________________________________________________________________________________________


#Avalição
#_________________________________________________________________________________________________________

def avaliarLivro(request):
    try:            
        if not all([request.POST['id'], request.POST['nota']]):
            raise Exception('Avalie o livro!')
        
        if Avaliacao.objects.filter(idLivro=request.POST['id'], idUsuario=request.session['usuario']['id']):
            avaliacao      = Avaliacao.objects.get(idLivro=request.POST['id'], idUsuario=request.session['usuario']['id']) 
            avaliacao.nota = int(request.POST['nota'])
        else:
            avaliacao           = Avaliacao()
            avaliacao.idLivro   = request.POST['id']
            avaliacao.idUsuario = request.session['usuario']['id']
            avaliacao.nota      = int(request.POST['nota'])
        
        avaliacao.validarDados()
        avaliacao.save()

        livro = Livros.objects.get(id=request.POST['id'])
        livro.notaMedia = livro.notaMedia()
        livro.save()

        return render(request, 'livros.html', {'sucesso': 'Livro avaliado com sucesso!', 'livros': Livros.objects.all()})
    except Exception as e:
        return render(request, 'livros.html', {'erro': e, 'livros': Livros.objects.all()})
    

#_________________________________________________________________________________________________________


#Resenha
#_________________________________________________________________________________________________________

def resenharLivro(request):
    return render(request, 'resenharLivro.html', {
        'livro'  : Livros.objects.get(id=request.POST['id']),
        'resenha': Resenha.objects.filter(idLivro=request.POST['id'], idUsuario=request.session['usuario']['id']).first()
    })

def resenha(request):    
    try:
        if (not request.POST['resenha']):
            raise Exception('Escreva a resenha!')
        
        if Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']):
            resenha = Resenha.objects.get(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id'])
            resenha.resenha = request.POST['resenha']
        else:
            resenha           = Resenha()
            resenha.idLivro   = request.POST['livro']
            resenha.idUsuario = request.session['usuario']['id']
            resenha.resenha   = request.POST['resenha']
        
        resenha.validarDados()
        resenha.save()
        
        return render(request, 'resenharLivro.html', {
            'sucesso': 'Resenha feita com sucesso!',
            'livro'  : Livros.objects.get(id=request.POST['livro']),
            'resenha': Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first()
        })
    except Exception as e:
        return render(request, 'resenharLivro.html', {
            'erro'   : e,
            'livro'  : Livros.objects.get(id=request.POST['livro']),
            'resenha': Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first()
        })