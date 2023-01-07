from django.db import models
from django.core.exceptions import ValidationError


def validar_numero(value):
    if not value.isdigit():
        raise ValidationError('O número de telefone deve conter apenas NÚMEROS!')


class Contato(models.Model):
    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30, blank = True)
    empresa = models.CharField(max_length = 60, blank = True)
    cargo = models.CharField(max_length = 60, blank = True)
    email = models.CharField(max_length = 60, blank = True)
    telefone = models.CharField('Número | Ex.: 85912345678', max_length = 11, validators = [validar_numero])
    aniversario = models.DateField(blank = True)
    observaçao = models.TextField(blank = True)

    def __str__(self):
        return self.nome
