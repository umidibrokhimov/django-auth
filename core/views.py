from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .forms import *

class Home(TemplateView):
    template_name = 'index.html'

class SignIn(CreateView):
    form_class = CustomUserCreationForm
    success_url = '/accounts/login'
    template_name = 'registration/signin.html'