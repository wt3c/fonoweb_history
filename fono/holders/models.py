from django.db import models


class Holder(models.Model):
    TP_PESSOA = [
        ('J', 'JURIDÍCA'),
        ('F', 'FÍSICA'),
    ]

    name = models.CharField('Nome', max_length=100)
    cod_ecad = models.IntegerField('Cód.ECAD', null=True)
    type_doc = models.CharField('TP_Pessoa', max_length=1, choices=TP_PESSOA, default='FÍSICA')
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
        verbose_name = 'Titular'
        verbose_name_plural = 'Titulares'

    def __str__(self):
        return self.name
