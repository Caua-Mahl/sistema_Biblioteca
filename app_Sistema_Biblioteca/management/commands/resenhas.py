from django.core.management.base import BaseCommand
from faker import Faker
from app_Sistema_Biblioteca.Models.Resenha import Resenha

import random

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        for _ in range(300):
            resenha = Resenha(
                idLivro=random.randint(1, 100),
                idUsuario=random.randint(1, 100),
                resenha=fake.text(max_nb_chars=200),
            )
            resenha.validarDados()
            resenha.save()
