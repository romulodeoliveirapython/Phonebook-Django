from django.shortcuts import render
from django.views.generic import ListView
from phonebook.models import Contato


class ContatoList(ListView):
    model = Contato
    queryset = Contato.objects.all()