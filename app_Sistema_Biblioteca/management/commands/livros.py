from django.core.management.base import BaseCommand
from faker import Faker
from app_Sistema_Biblioteca.Models.Livros import Livros

import random

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        generos = ['Ação', 'Aventura', 'Comédia', 'Drama', 'Ficção Científica', 'Romance', 'Terror']

        for _ in range(100):  
            livro = Livros(
                titulo=fake.first_name() + ' ' + fake.word(ext_word_list=['e o segredo', 'na terra do nunca', 'e a jornada do herói']),
                autor=fake.name(),
                genero=random.choice(generos),
                lancamento=fake.date_between(start_date='-30y', end_date='today'),
            )
            livro.save()