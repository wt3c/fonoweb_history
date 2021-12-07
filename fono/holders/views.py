from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView

from .forms import HoldersForm


class New(LoginRequiredMixin, FormView):
    template_name = 'holders/holders_form.html'
    login_url = 'login'
    form_class = HoldersForm
    success_url = '/new/'

    def form_valid(self, form):
        return super().form_valid(form)
#
#
# class New(LoginRequiredMixin, TemplateView):
#     template_name = 'holders/holders_form.html'
#     login_url = 'login'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
