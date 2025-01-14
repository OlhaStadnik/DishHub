from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .forms import RegisterForm
from .models import CookUser


class CookUserListView(LoginRequiredMixin, generic.ListView):
    model = CookUser
    template_name = "accounts/cook_list.html"
    queryset = CookUser.objects.all().prefetch_related("dishes")


class CookUserRegisterView(CreateView):
    model = CookUser
    form_class = RegisterForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("recipe_manager:home")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CookUserProfileView(LoginRequiredMixin, generic.DetailView):
    model = CookUser
    template_name = "accounts/profile.html"
    context_object_name = "user"

    def get_object(self, queryset=None) -> CookUser:
        return self.request.user


class CookUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CookUser
    fields = ["username", "email", "years_of_experience"]
    template_name = "accounts/update_profile.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None) -> CookUser:
        return self.request.user


class CookUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = get_user_model()
    template_name = "accounts/profile.html"
    context_object_name = "user"
