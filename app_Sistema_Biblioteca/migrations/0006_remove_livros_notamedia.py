# Generated by Django 5.0.3 on 2024-04-03 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_Sistema_Biblioteca', '0005_rename_texto_resenha_resenha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livros',
            name='notaMedia',
        ),
    ]
