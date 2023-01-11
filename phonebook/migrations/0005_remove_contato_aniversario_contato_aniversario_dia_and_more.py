# Generated by Django 4.1.5 on 2023-01-11 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0004_alter_contato_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='aniversario',
        ),
        migrations.AddField(
            model_name='contato',
            name='aniversario_dia',
            field=models.CharField(blank=True, choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=2),
        ),
        migrations.AddField(
            model_name='contato',
            name='aniversario_mes',
            field=models.CharField(blank=True, choices=[('jan', 'Janeiro'), ('fev', 'Fevereiro'), ('mar', 'Março'), ('abr', 'Abril'), ('mai', 'Maio'), ('jun', 'Junho'), ('jul', 'Junho'), ('ago', 'Agosto'), ('set', 'Setembro'), ('out', 'Outubro'), ('nov', 'Novembro'), ('dez', 'Dezembro')], max_length=3),
        ),
    ]