from django.db import models
from django.core.exceptions import ValidationError


def validar_numero(value):
    if not value.isdigit():
        raise ValidationError('O número de telefone deve conter apenas NÚMEROS!')


class Contato(models.Model):
    mes = [
        ('jan', 'Janeiro'),
        ('fev', 'Fevereiro'),
        ('mar', 'Março'),
        ('abr', 'Abril'),
        ('mai', 'Maio'),
        ('jun', 'Junho'),
        ('jul', 'Junho'),
        ('ago', 'Agosto'),
        ('set', 'Setembro'),
        ('out', 'Outubro'),
        ('nov', 'Novembro'),
        ('dez', 'Dezembro'),
    ]

    dia = [
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
    ]

    nome = models.CharField(max_length = 30)
    sobrenome = models.CharField(max_length = 30, blank = True)
    empresa = models.CharField(max_length = 60, blank = True)
    cargo = models.CharField(max_length = 60, blank = True)
    email = models.CharField(max_length = 60, blank = True)
    telefone = models.CharField('Número | Ex.: 85912345678', max_length = 11, validators = [validar_numero])
    aniversario_dia = models.CharField(max_length = 2, choices = dia, blank = True)
    aniversario_mes = models.CharField(max_length = 3, choices = mes, blank = True)
    observaçao = models.TextField(blank = True)

    def __str__(self):
        return "{} - {}".format(self.nome, self.telefone)
