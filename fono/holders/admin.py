from django.contrib import admin
from fono.holders.models import Holder
from fono.holders.models import Pseudonym


class HolderModelAdmin(admin.ModelAdmin):
    list_display = ('cod_ecad', 'name', 'type_doc', 'cpf', 'cnpj', 'ifpi', 'radical_ifpi', 'is_publisher',
                    'is_record_producer', 'is_interpreter', 'is_author', 'is_musician', 'note')
    list_filter = ('cod_ecad', 'name',)
    search_fields = ('cod_ecad', 'name',)


admin.site.register(Holder, HolderModelAdmin)
admin.site.register(Pseudonym)
