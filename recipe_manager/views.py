from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View

from recipe_manager.forms import DishCreateForm, DishSearchForm, DishTypeSearchForm
from recipe_manager.models import DishType, Dish


class HomeView(generic.TemplateView):
    template_name = "home.html"


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "recipe_manager/dish_type_list.html"
    context_object_name = "dish_types"
    queryset = DishType.objects.all()
    paginate_by = 6

    def get_context_data(self, object_list=None, **kwargs):
        context = super(DishTypeListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishTypeSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = DishType.objects.all()
        form = DishTypeSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset


class DishTypeDetailView(generic.DetailView):
    model = DishType
    template_name = "recipe_manager/dish_type_detail.html"
    context_object_name = "dish_type"


class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name"]
    template_name = "recipe_manager/dish_type_form.html"
    success_url = reverse_lazy("recipe_manager:dish-type-list")


class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "recipe_manager/dish_type_form.html"
    success_url = reverse_lazy("recipe_manager:dish-type-list")


class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "recipe_manager/dish_type_confirm_delete.html"
    success_url = reverse_lazy("recipe_manager:dish-type-list")


# Dish Views
class DishListView(generic.ListView):
    model = Dish
    template_name = "recipe_manager/dish_list.html"
    context_object_name = "dishes"
    queryset = Dish.objects.all().prefetch_related("cooks")
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = DishSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        form = DishSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(name__icontains=form.cleaned_data["name"])
        return self.queryset


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "recipe_manager/dish_detail.html"
    context_object_name = "dish"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = ["name", "description", "dish_type", "price", "cooks"]
    template_name = "recipe_manager/dish_form.html"
    success_url = reverse_lazy("recipe_manager:dish-list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = ["name", "description", "dish_type", "price", "cooks"]
    template_name = "recipe_manager/dish_form.html"
    success_url = reverse_lazy("recipe_manager:dish-list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "recipe_manager/dish_confirm_delete.html"
    success_url = reverse_lazy("recipe_manager:dish-list")
