from django.db import models

class Usuario(models.Model):
    id    = models.AutoField(primary_key=True)
    nome  = models.CharField(max_length=100)
    email = models.EmailField()
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome