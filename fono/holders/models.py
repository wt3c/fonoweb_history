from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import resolve_url as r

from fono.core.managers import KindQuerySet


class Society(models.Model):
    initials = models.CharField('SIGLA', max_length=50)
    name = models.CharField('NOME', max_length=200)

    class Meta:
        verbose_name = 'Sociedade'
        verbose_name_plural = 'Sociedades'

    def __str__(self):
        return self.name

    def get_all_society(self):
        return Society.objects.all()


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone')
    )
    holder = models.ForeignKey('Holder', on_delete=models.CASCADE, verbose_name='Titular')
    kind = models.CharField('Tipo', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=50)

    # Explicitando o modulo objects
    objects = KindQuerySet.as_manager()

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Pseudonym(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    holder = models.ForeignKey('Holder', blank=True, null=True, verbose_name='Titular', on_delete=models.CASCADE)
    pseudonym = models.CharField('Pseudônimo', max_length=100)
    is_main = models.BooleanField('É o Principal', default=False)

    class Meta:
        verbose_name = 'Pseudônimo'
        verbose_name_plural = 'Pseudônimos'

    def __str__(self):
        return self.pseudonym


class Holder(models.Model):
    TP_PESSOA = [
        ('J', 'JURIDÍCA'),
        ('F', 'FÍSICA'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')
    society = models.ForeignKey('Society', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Sociedade')
    cod_ecad = models.IntegerField('Cód.ECAD', blank=True, null=True)
    name = models.CharField('Nome', max_length=100)
    type_doc = models.CharField('Tipo Pessoa', max_length=1, choices=TP_PESSOA, default='F')
    # TODO: Criar validators para CPF e CNPJ
    # cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    cpf = models.CharField('CPF', max_length=11, blank=True)
    cnpj = models.CharField('CNPJ', max_length=16, blank=True)
    ifpi = models.CharField('IFPI', max_length=3, blank=True)
    radical_ifpi = models.CharField('RADICAL IFPI', max_length=2, blank=True)
    is_publisher = models.BooleanField('É EDITORA', default=False)
    is_record_producer = models.BooleanField('É PRODUTOR FONOGRAFICO', default=False)
    is_interpreter = models.BooleanField('É INTERPRETE', default=False)
    is_author = models.BooleanField('É AUTOR', default=False)
    is_musician = models.BooleanField('É MUSICO', default=False)
    is_deleted = models.BooleanField(default=False)
    note = models.TextField('OBSERVAÇÃO', blank=True)

    class Meta:
        verbose_name = 'titular'
        verbose_name_plural = 'titulares'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('holder:new')
