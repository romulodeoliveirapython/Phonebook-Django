from django import forms
from phonebook.models import Contato


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('user',)

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if not telefone.isdigit():
            self.add_error('telefone', 'O número de telefone deve conter apenas caracteres numéricos!')
        return telefone