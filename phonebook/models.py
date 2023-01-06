from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30, blank = True)
    empresa = models.CharField(max_length = 60, blank = True)
    cargo = models.CharField(max_length = 60, blank = True)
    email = models.CharField(max_length = 60, blank = True)
    telefone = models.CharField(max_length = 15)
    aniversário = models.DateField(blank = True)
    observação = models.TextField(blank = True)