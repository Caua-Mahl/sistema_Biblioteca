from django.db import models
from django.contrib.auth.models import User
import re
from app_Sistema_Biblioteca.Models.Avaliacao import Avaliacao
from app_Sistema_Biblioteca.Models.Resenha import Resenha


class Usuario(models.Model):
    nome    = models.CharField(max_length=100)
    email   = models.EmailField(max_length=100)
    senha   = models.CharField(max_length=20)
    admin   = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
    def validarDadosCadastro(self, confirmarSenha):
        self.validarNome()
        self.validarEmail()
        self.validarSenha(confirmarSenha)

        if Usuario.objects.filter(nome=self.nome).exists():
            raise Exception('Nome já cadastrado, Tente outro!')
        
        if Usuario.objects.filter(email=self.email).exists():
            raise Exception('Email já cadastrado, Tente outro!')
        

    def validarDadosLogin(self):
        self.validarEmail()
        self.validarSenha(cadastro=False)

    def validarSenha(self, confirmarSenha="", cadastro=True):
        if len(self.senha) < 6:
            raise Exception('Senha deve ter no mínimo 6 caracteres!')

        if len(self.senha) > 20:
            raise Exception('Senha deve ter no máximo 20 caracteres!')
        
        if cadastro and self.senha != confirmarSenha:
            raise Exception('Senhas não conferem!')
        
        if self.senha == self.nome or self.senha == self.email:
            raise Exception('Senha não pode ser igual ao nome/email!')
    
    def validarEmail(self):
        if not '@' in self.email or not '.' in self.email:
            raise Exception('Email inválido!')
        
        if len(self.email) < 5:
            raise Exception('Email deve ter no mínimo 5 caracteres!')
        
        if len(self.email) > 100:
            raise Exception('Email deve ter no máximo 100 caracteres!')
        
    def validarNome(self):   
        if len(self.nome) > 100:
            raise Exception('Nome deve ter no máximo 100 caracteres!')
        
        if '  ' in self.nome:
            raise Exception('Nome não pode conter mais de um espaço seguido!')
        
        if len(self.nome.strip()) < 3:
            raise Exception('Nome deve ter no mínimo 3 caracteres!')
        
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', self.nome.strip()):
            raise Exception('Nome deve conter apenas letras e espaços!')


    @staticmethod
    def puxarUsuarios(idLivro):
        usuarios = Usuario.objects.all()

        for usuario in usuarios:
            avaliacoes = Avaliacao.objects.filter(idUsuario=usuario.id, idLivro=idLivro)
            resenhas   = Resenha.objects.filter(idUsuario=usuario.id, idLivro=idLivro)

            if avaliacoes:
                usuario.nota = avaliacoes[0].nota
            
            if resenhas:
                usuario.resenha = resenhas[0].resenha
            
        return usuarios
        
