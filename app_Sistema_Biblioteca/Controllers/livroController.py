from django.shortcuts                        import render
from django.contrib.auth                     import authenticate, login
from app_Sistema_Biblioteca.Models.Livros    import Livros
from app_Sistema_Biblioteca.Models.Avaliacao import Avaliacao
from app_Sistema_Biblioteca.Models.Resenha   import Resenha
from app_Sistema_Biblioteca.Models.Usuario   import Usuario

def livrosLista(request):
    if 'usuario' not in request.session:
        return render(request, 'login.html', { 'erro' : 'Você não está logado!' })
    
    return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})


""""
 _____________________________________________________________________ 

ADMIN LIVROS
 _____________________________________________________________________ 
"""""

def adminLivro(request):
    if 'usuario' not in request.session:
        return render(request, 'login.html', { 'erro' : 'Você não está logado!' })
    
    if request.session['usuario']['admin'] == False:
        return render(request, 'livrosLista.html', {'livros': Livros.objects.all()})

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
    


""""
 _____________________________________________________________________ 

AO CLICAR EM VER MAIS DE UM LIVRO EXPECIFICO, ABAIXO ENVOLVE A PAGINA LIVRO.HTML
 _____________________________________________________________________ 
"""""

def livro(request):
    if 'usuario' not in request.session:
        return render(request, 'login.html', { 'erro' : 'Você não está logado!' })

    return render(request, 'livro.html', {
        'livro'     : Livros.objects.get(id=request.POST['livro']),
        'resenha'   : Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
        'avaliacao' : Avaliacao.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
        'usuarios'  : Usuario.puxarUsuarios(idLivro=request.POST['livro']),
    })

def avaliarLivro(request):
    try:            
        if not all([request.POST['livro'], request.POST['nota']]):
            raise Exception('Avalie o livro!')
        
        if Avaliacao.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']):
            avaliacao      = Avaliacao.objects.get(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']) 
            avaliacao.nota = int(request.POST['nota'])
        else:
            avaliacao           = Avaliacao()
            avaliacao.idLivro   = request.POST['livro']
            avaliacao.idUsuario = request.session['usuario']['id']
            avaliacao.nota      = int(request.POST['nota'])
        
        avaliacao.validarDados()
        avaliacao.save()

        livro           = Livros.objects.get(id=request.POST['livro'])
        livro.notaMedia = livro.notaMedia()
        livro.save()

        return render(request, 'livro.html', {
            'sucesso'   : 'Livro avaliado com sucesso!',
            'livro'     : Livros.objects.get(id=request.POST['livro']),
            'resenha'   : Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
            'avaliacao' : Avaliacao.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
            'usuarios'  : Usuario.puxarUsuarios(idLivro=request.POST['livro']),

        })
    except Exception as e:
        return render(request, 'livro.html', {
            'erro'      : e, 
            'livro'     : Livros.objects.get(id=request.POST['livro']),
            'resenha'   : Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
            'avaliacao' : Avaliacao.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
            'usuarios'  : Usuario.puxarUsuarios(idLivro=request.POST['livro']),

        })
    
def resenha(request):    
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
    
    return render(request, 'livro.html', {
        'sucesso'   : 'Resenha feita com sucesso!',
        'livro'     : Livros.objects.get(id=request.POST['livro']),
        'resenha'   : Resenha.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
        'avaliacao' : Avaliacao.objects.filter(idLivro=request.POST['livro'], idUsuario=request.session['usuario']['id']).first(),
        'usuarios'  : Usuario.puxarUsuarios(idLivro=request.POST['livro']),
    })
