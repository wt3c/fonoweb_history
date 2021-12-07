from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

from .forms import HoldersForm
from .models import Holder


class HolderCreate(LoginRequiredMixin, CreateView):
    template_name = 'holders/holders_form.html'
    login_url = 'login'
    form_class = HoldersForm
    model = Holder

    def form_valid(self, form):
        return super().form_valid(form)
