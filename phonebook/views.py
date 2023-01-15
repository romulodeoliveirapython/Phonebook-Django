from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from phonebook.models import Contato
from phonebook.forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from urllib import request


def home(request):
    return render(request, 'phonebook/home.html')


@method_decorator(login_required, name='dispatch')
class ContatoList(ListView):
    model = Contato

    def get_queryset(self):
        return Contato.objects.filter(usuario = self.request.user)


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

    def novoContato(request):

        if request.method == 'POST':
            form = ContatoForm(request.POST)

            if form.is_valid():
                contato = form.save(commit = False)
                contato.usuario = request.user
                contato.save()
                return redirect('phonebook:list')

        else:
            form = ContatoForm()
            return render(request, 'phonebook:list', {'form': form})


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