from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from phonebook.models import Contato
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from phonebook.forms import ContatoForm


def home(request):
    return render(request, 'phonebook/home.html')


@method_decorator(login_required, name='dispatch')
class ContatoList(ListView):
    model = Contato

    def get_queryset(self):
        return Contato.objects.filter(user = self.request.user)


@method_decorator(login_required, name='dispatch')
class ContatoDetail(DetailView):
    model = Contato
    queryset = Contato.objects.all()
    template_name = 'phonebook/contato_detail.html'


@method_decorator(login_required, name='dispatch')
class ContatoCreate(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'phonebook/create_contact.html'
    success_url = reverse_lazy('phonebook:list')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            return super().form_valid(form)
        else:
            return redirect('login')


@method_decorator(login_required, name='dispatch')
class ContatoUpdate(UpdateView):
    model: Contato
    queryset = Contato.objects.all()
    success_url = reverse_lazy('phonebook:list')
    template_name = 'phonebook/contato_update.html'
    form_class = ContatoForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ContatoDelete(DeleteView):
    model = Contato
    fields = '__all__'
    success_url = reverse_lazy('phonebook:list')


def handler404(request, exception):
    return render(request, 'phonebook/404.html')