from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, View
from django.contrib.auth.models import User
from django.forms.models import inlineformset_factory
from extra_views import FormSetView, InlineFormSetFactory, CreateWithInlinesView

from .forms import HolderForm, PseudonymForm
from .models import Holder, Pseudonym


class PseudonymInLine(InlineFormSetFactory):
    # https://django-extra-views.readthedocs.io/en/latest/pages/getting-started.html
    model = Pseudonym
    fields = ['pseudonym', 'is_main']
    factory_kwargs = {'extra': 1, 'max_num': None,
                      'can_order': False, 'can_delete': False}


class HolderCreate(LoginRequiredMixin, CreateWithInlinesView):
    template_name = 'holders/holders_form.html'
    login_url = 'login'
    form_class = HolderForm
    model = Holder
    exclude = ('owner',)
    inlines = [PseudonymInLine]

    def form_valid(self, form):
        from pprint import pprint
        print('**************************************')
        pprint(self.request.POST)
        print('**************************************')

        form.instance.owner = self.request.user
        return super().form_valid(form)


def holder_create(request):
    """                   FORMSET PADRÃO
                        https://www.youtube.com/watch?v=_k-98frcD_M
                        https://github.com/elo80ka/django-dynamic-formset/blob/master/docs/usage.rst
    """
    if request.method == "GET":
        form = HolderForm()

        form_pseudo_factory = inlineformset_factory(Holder, Pseudonym, form=PseudonymForm, extra=1)
        form_pseudo = form_pseudo_factory()

        context = {'form': form, 'form_pseudo': form_pseudo}
        return render(request, 'holders/holders_form.html', context)

    elif request.method == "POST":
        form = HolderForm(request.POST)
        form.instance.owner = request.user

        form_pseudo_factory = inlineformset_factory(Holder, Pseudonym, form=PseudonymForm)
        form_pseudo = form_pseudo_factory(request.POST)

        if form.is_valid() and form_pseudo.is_valid():
            holder = form.save()
            form_pseudo.instance = holder
            form_pseudo.save()

            from pprint import pprint
            print('**************************************')
            pprint(request.POST)
            print('**************************************')

            return redirect(reverse('holder:new'))
        else:
            context = {
                'form': form,
                'form_pseudo': form_pseudo
            }
            return render(request, 'holders/holders_form.html', context)
