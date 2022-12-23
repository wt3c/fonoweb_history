from django.contrib import admin

from fono.holders.models import Contact
from fono.holders.models import Holder
from fono.holders.models import Pseudonym
from fono.holders.models import Society


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1


class PseudonymInLine(admin.TabularInline):
    model = Pseudonym
    extra = 1


class HolderModelAdmin(admin.ModelAdmin):
    inlines = [PseudonymInLine, ContactInLine]

    list_display = ('cod_ecad', 'name', 'type_doc', 'cpf', 'cnpj', 'ifpi', 'radical_ifpi', 'is_publisher',
                    'is_record_producer', 'is_interpreter', 'is_author', 'is_musician', 'note')

    list_filter = ('cod_ecad', 'name',)
    search_fields = ('cod_ecad', 'name',)


admin.site.register(Holder, HolderModelAdmin)
admin.site.register(Pseudonym)
admin.site.register(Society)
admin.site.register(Contact)
