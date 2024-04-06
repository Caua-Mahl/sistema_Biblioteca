from django.contrib                     import admin
from django.urls                        import path
from app_Sistema_Biblioteca.Controllers import cadastroController as cadastro
from app_Sistema_Biblioteca.Controllers import loginController    as login
from app_Sistema_Biblioteca.Controllers import livroController    as livro


urlpatterns = [
    path('admin/',         admin.site.urls),
    path('cadastro/',      cadastro.cadastro,      name='cadastro'),
    path('cadastrar/',     cadastro.cadastrar,     name='cadastrar'),

    path('',               login.login,            name='login'),
    path('logar/',         login.logar,            name='logar'),
    path('logout/',        login.logout,           name='logout'),

    path('livros/',        livro.livrosLista,      name='livros'),
    path('livro/',         livro.livro,            name='livro'),
    path('adminLivro/',    livro.adminLivro,       name='adminLivro'),
    path('editarLivro/',   livro.editarLivro,      name='editarLivro'),
    path('excluirLivro/',  livro.excluirLivro,     name='excluirLivro'),
    path('avaliarLivro/',  livro.avaliarLivro,     name='avaliarLivro'),
    path('resenha/',       livro.resenha,          name='resenha'),
]
