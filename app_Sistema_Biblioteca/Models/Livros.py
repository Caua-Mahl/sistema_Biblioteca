from django.db import models
import re
from app_Sistema_Biblioteca.Models.Avaliacao import Avaliacao

class Livros(models.Model):
    titulo     = models.CharField(max_length=100)
    autor      = models.CharField(max_length=100)
    genero     = models.CharField(max_length=100)
    lancamento = models.DateField()
    notaMedia  = models.FloatField()
    
    def __str__(self):
        return self.titulo
    
    def validarDados(self):
        self.validarTitulo()
        self.validarAutor()
        self.validarGenero()
        #self.validarLancamento()

    def validarTitulo(self):
        if len(self.titulo) < 3:
            raise Exception('Título deve ter no mínimo 3 caracteres!')
        
        if len(self.titulo) > 100:
            raise Exception('Título deve ter no máximo 100 caracteres!')
        
        if '  ' in self.titulo:
            raise Exception('Título não pode conter mais de um espaço seguido!')
        
    def validarAutor(self):   
        if len(self.autor) > 100:
            raise Exception('Nome deve ter no máximo 100 caracteres!')
        
        if '  ' in self.autor:
            raise Exception('Nome não pode conter mais de um espaço seguido!')
        
        if len(self.autor.strip()) < 3:
            raise Exception('Nome deve ter no mínimo 3 caracteres!')
        
        if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$', self.autor.strip()):
            raise Exception('Nome deve conter apenas letras e espaços!')

    def validarGenero(self):
        if self.genero not in ['Ação', 'Aventura', 'Comédia', 'Drama', 'Ficção Científica', 'Romance', 'Terror']:
            raise Exception('Gênero inválido!')
        
    #def validarLancamento(self):
        #impedir de criar livros com data de lançamento futura

    def notaMedia(self):
        avaliacoes = Avaliacao.objects.filter(idLivro=self.id)

        if not avaliacoes:
            return 0.0
        
        return round(sum([avaliacao.nota for avaliacao in avaliacoes]) / len(avaliacoes), 1)



