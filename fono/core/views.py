from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, resolve_url as r
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View, TemplateView
from django.views.generic.edit import FormView


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'login'

    # redirect_field_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

# TODO .: Alterar as funções login e logout para class mixins.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(r('home'))
        else:
            return render(request, "core/login.html", {"form": form})

    return render(request, "core/login.html", {"form": AuthenticationForm()})


# class Login(FormView):
#     template_name = 'core/login.html'
#     form_class = AuthenticationForm
#     success_url = '/home_user/'
#
#     def form_valid(self, form):
#         return super().form_valid(form)


def logout(request):
    auth_logout(request)
    return render(request, 'core/login.html', {'form': AuthenticationForm()})
