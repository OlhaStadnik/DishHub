from django.contrib.auth import login
from django.views.generic import FormView

from django.urls import reverse_lazy
from .forms import RegisterForm

class UserRegisterView(FormView):
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)