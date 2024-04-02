from django.contrib import admin
from django.urls import path
from app_Sistema_Biblioteca import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('cadastro/', views.cadastro, name='cadastro'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),

    path('login/', views.login, name='login'),
    path('logar/', views.logar, name='logar'),
    path('logout/', views.logout, name='logout'),

    path('livros/', views.livros, name='livros'),
    path('cadastrarLivro/', views.cadastrarLivro, name='cadastrarLivro'),
    
]
