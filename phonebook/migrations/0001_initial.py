# Generated by Django 4.1.5 on 2023-01-07 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(blank=True, max_length=30)),
                ('empresa', models.CharField(blank=True, max_length=60)),
                ('cargo', models.CharField(blank=True, max_length=60)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('telefone', models.CharField(max_length=15)),
                ('aniversario', models.DateField(blank=True)),
                ('observaçao', models.TextField(blank=True)),
            ],
        ),
    ]
