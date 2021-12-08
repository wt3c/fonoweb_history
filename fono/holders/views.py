from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib.auth.models import User

from .forms import HolderForm
from .models import Holder


class HolderCreate(LoginRequiredMixin, CreateView):
    template_name = 'holders/holders_form.html'
    login_url = 'login'
    form_class = HolderForm
    model = Holder
    exclude = ('owner',)
    def form_valid(self, form):
        print('**************************************', self.request.user)
        # user = User.objects.get(pk=1)

        form.instance.owner = self.request.user
        return super().form_valid(form)
