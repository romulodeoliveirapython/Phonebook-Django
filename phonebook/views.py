from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from phonebook.models import Contato
from django.urls import reverse_lazy


class ContatoList(ListView):
    model = Contato
    queryset = Contato.objects.all()


class ContatoDetail(DetailView):
    model = Contato
    queryset = Contato.objects.all()
    template_name = 'phonebook/contato_detail.html'


class ContatoCreate(CreateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')


class ContatoUpdate(UpdateView):
    model: Contato
    fields = '__all__'
    queryset = Contato.objects.all()
    success_url = reverse_lazy('phonebook:list')
    template_name = 'phonebook/contato_update.html'

class ContatoDelete(DeleteView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')
    