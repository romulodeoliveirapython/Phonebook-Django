from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from phonebook.models import Contato
from django.urls import reverse_lazy


class ContatoList(ListView):
    model = Contato
    queryset = Contato.objects.all()


class ContatoCreate(CreateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')


class ContatoUpdate(UpdateView):
    model: Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')