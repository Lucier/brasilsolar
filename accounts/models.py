import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Apelido / Usuario' , max_length=30, unique=True, validators = [
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'Informe um nome de usuário válido',
                'Este valor deve conter apenas letras, numeros e os caracteres: @/./+/-/_.',
                'invalid'
            )
        ], help_text="Um nome curto que será usado para identifica-lo de forma única na plataforma"
    )
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', unique=True)
    cpf = models.CharField('CPF', max_length=20, blank=True)
    endereco = models.CharField('Endereco', max_length=100, blank=True)
    numero = models.CharField('Número', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=100, blank=True)
    cidade = models.CharField('Cidade', max_length=100, blank=True)
    estado = models.CharField('Estado', max_length=100, blank=True)
    cep = models.CharField('CEP', max_length=20, blank=True)
    is_staff = models.BooleanField('Equipe', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    
    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return str(self)
    
    def get_short_name(self):
        return str(self).split(" ")[0]
