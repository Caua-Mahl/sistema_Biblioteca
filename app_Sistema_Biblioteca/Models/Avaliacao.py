from django.db import models
import re

class Avaliacao(models.Model):
    idLivro   = models.IntegerField()
    idUsuario = models.IntegerField()
    nota      = models.IntegerField()

    def __str__(self):
        return str(self.idLivro) + ' - ' + str(self.idUsuario)
    
    def validarDados(self):
        if self.nota < 0 or self.nota > 10:
            raise Exception('Nota deve ser entre 0 e 10!')
