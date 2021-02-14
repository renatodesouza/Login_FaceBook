from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView




class IndexView(TemplateView):
    template_name = 'index.html'

class AutenticacaoView(TemplateView):
    template_name = 'login.html'

class UserTemplateView(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


def login_user(request):
    username = request.GET['username']
    password = request.GET['password']

    user = authenticate(request, username=username, password=password)
    print("Usuario: ", user)
    if user is not None:
        login(request, user)
        return redirect('user')
    else:
        context = 'login invalido'
        return render(request, 'index.html', {'context':context})



