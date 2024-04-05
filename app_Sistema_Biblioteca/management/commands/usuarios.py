from django.core.management.base import BaseCommand
from faker import Faker
from app_Sistema_Biblioteca.Models.Usuario import Usuario

import random

class Command(BaseCommand):
    help = 'Populates the database with fake data'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        for _ in range(100):
            usuario = Usuario(
                nome=fake.name(),
                email=fake.email(),
                senha=fake.password(),
            )
            usuario.save()
