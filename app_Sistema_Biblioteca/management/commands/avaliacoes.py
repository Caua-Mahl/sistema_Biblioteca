from django.core.management.base import BaseCommand
from faker import Faker
from app_Sistema_Biblioteca.Models.Avaliacao import Avaliacao

import random

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        for _ in range(500):
            avaliacao = Avaliacao(
                idLivro=random.randint(1, 100),
                idUsuario=random.randint(1, 100),
                nota=random.randint(0, 10),
            )
            avaliacao.validarDados()
            avaliacao.save()
