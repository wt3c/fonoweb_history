from django.contrib import admin
from fono.holders.models import Holder


class HolderModelAdmin(admin.ModelAdmin):
    list_display = ('cod_ecad', 'name', 'type_doc', 'cpf', 'cnpj', 'ifpi', 'radical_ifpi', 'is_editora',
                    'is_produtor_fono', 'is_interprete', 'is_autor', 'is_musico', 'is_deleted', 'observacao')
    list_filter = ('cod_ecad', 'name',)
    search_fields = ('cod_ecad', 'name',)


admin.site.register(Holder, HolderModelAdmin)
