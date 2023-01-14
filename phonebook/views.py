from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from phonebook.models import Contato
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib import request


def home(request):
    return render(request, 'phonebook/home.html')


@method_decorator(login_required, name='dispatch')
class ContatoList(ListView):
    model = Contato
    queryset = Contato.objects.all()


@method_decorator(login_required, name='dispatch')
class ContatoDetail(DetailView):
    model = Contato
    queryset = Contato.objects.all()
    template_name = 'phonebook/contato_detail.html'


@method_decorator(login_required, name='dispatch')
class ContatoCreate(CreateView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')


@method_decorator(login_required, name='dispatch')
class ContatoUpdate(UpdateView):
    model: Contato
    fields = '__all__'
    queryset = Contato.objects.all()
    success_url = reverse_lazy('phonebook:list')
    template_name = 'phonebook/contato_update.html'


@method_decorator(login_required, name='dispatch')
class ContatoDelete(DeleteView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')


def handler404(request, exception):
    return render(request, 'phonebook/404.html')