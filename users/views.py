from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import views

from .models import UserProfile
from .forms import RegisterUserForm


class LoginUserView(views.LoginView):
    template_name = 'users/login.html'


class RegisterUserView(CreateView):
    model = UserProfile
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:login')