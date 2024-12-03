from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from django.views.generic import FormView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy
from .forms import RegisterForm
from .models import CookUser
from django.contrib.auth import get_user_model


class CookUserListView(LoginRequiredMixin, generic.ListView):
    model = CookUser
    template_name = "accounts/cook_list.html"

class CookUserRegisterView(CreateView):
    model = CookUser
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("recipe_manager:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CookUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CookUser
    fields = ["username", "email", "years_of_experience"]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("profile")

    def get_object(self):
        return self.request.user

class CookUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "accounts/profile.html"
    context_object_name = "user"
    # queryset = CookUser.objects.prefetch_related("dishes") # список страв

