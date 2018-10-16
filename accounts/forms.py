from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'cpf', 'endereco',  'numero', 'bairro', 'cidade', 'estado', 'cep']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'cpf', 'endereco', 'numero', 'bairro', 'cidade', 'estado',
                    'cep', 'is_active', 'is_staff']
