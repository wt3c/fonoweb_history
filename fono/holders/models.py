from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r


class Holder(models.Model):
    TP_PESSOA = [
        ('J', 'JURIDÍCA'),
        ('F', 'FÍSICA'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=100)
    cod_ecad = models.IntegerField('Cód.ECAD', blank=True, null=True)
    type_doc = models.CharField('Tipo Pessoa', max_length=1, choices=TP_PESSOA, default='F')
    # TODO: Criar validators para CPF e CNPJ
    # cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    cpf = models.CharField('CPF', max_length=11, blank=True)
    cnpj = models.CharField('CNPJ', max_length=16, blank=True)
    ifpi = models.CharField('IFPI', max_length=3, blank=True)
    radical_ifpi = models.CharField('RADICAL IFPI', max_length=2, blank=True)
    is_editora = models.BooleanField('É EDITORA', default=False)
    is_produtor_fono = models.BooleanField('É PRODUTOR FONOGRAFICO', default=False)
    is_interprete = models.BooleanField('É INTERPRETE', default=False)
    is_autor = models.BooleanField('É AUTOR', default=False)
    is_musico = models.BooleanField('É MUSICO', default=False)
    is_deleted = models.BooleanField(default=False)
    observacao = models.TextField('OBSERVAÇÃO', blank=True)

    class Meta:
        verbose_name = 'titular'
        verbose_name_plural = 'titulares'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('holder:new')
