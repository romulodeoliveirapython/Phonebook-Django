from django import forms
from phonebook.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        field = '__all__'
