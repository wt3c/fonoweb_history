from django.contrib.auth import login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect, resolve_url as r
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import View, TemplateView


class Home(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


def login(request):
    if request.method == 'POST':

        form = AuthenticationForm(data=request.POST)

        if not form.is_valid():
            return render(request, "core/login.html", {"form": form})

        auth_login(request, form.get_user())
        return redirect(r('home'))
    return render(request, "core/login.html", {"form": AuthenticationForm()})


def logout(request):
    auth_logout(request)
    return render(request, 'core/login.html', {'form': AuthenticationForm()})
