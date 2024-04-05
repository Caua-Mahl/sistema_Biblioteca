from django.db import models

class Resenha(models.Model):
    idLivro   = models.IntegerField()
    idUsuario = models.IntegerField()
    resenha   = models.TextField()

    def __str__(self):
        return str(self.idLivro) + ' - ' + str(self.idUsuario)
    
    def validarDados(self):
        if len(self.resenha.strip()) < 10:
            raise Exception('Texto deve ter no mínimo 10 caracteres!')
        
        if len(self.resenha) > 2000:
            raise Exception('Texto deve ter no máximo 500 caracteres!')
          