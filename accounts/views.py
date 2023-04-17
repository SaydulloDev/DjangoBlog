from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterForm, CustomAuthenticationForm


# Create your views here.


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def custom_login(request):
    form = CustomAuthenticationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username is not None and password:
            user = authenticate(
                request, username=username, password=password
            )
            login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html", {"form": form})
