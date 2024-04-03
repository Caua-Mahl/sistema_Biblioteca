# Generated by Django 5.0.3 on 2024-04-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_Sistema_Biblioteca', '0003_livros'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLivro', models.IntegerField()),
                ('idUsuario', models.IntegerField()),
                ('nota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idLivro', models.IntegerField()),
                ('idUsuario', models.IntegerField()),
                ('texto', models.TextField()),
            ],
        ),
    ]
