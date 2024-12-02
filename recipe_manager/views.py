from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from recipe_manager.models import DishType, Dish


class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "recipe_manager/dish_type_list.html"
    context_object_name = "dish_types"
    queryset = DishType.objects.all()
    paginate_by = 5

class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = ["name"]
    template_name = "recipe_manager/dish_type_form.html"
    success_url = reverse_lazy("dishes:dish-type-list")

class DishTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = DishType
    fields = ["name"]
    template_name = "recipe_manager/dish_type_form.html"
    success_url = reverse_lazy("dishes:dish-type-list")

class DishTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = DishType
    template_name = "recipe_manager/dish_type_confirm_delete.html"
    success_url = reverse_lazy("dishes:dish-type-list")

# Dish Views
class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    template_name = "recipe_manager/dish_list.html"
    context_object_name = "dishes"
    queryset = Dish.objects.all()
    paginate_by = 5

class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    fields = ["name", "description", "type", "price", "is_vegetarian"]
    template_name = "recipe_manager/dish_form.html"
    success_url = reverse_lazy("dishes:dish-list")

class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    fields = ["name", "description", "type", "price", "is_vegetarian"]
    template_name = "recipe_manager/dish_form.html"
    success_url = reverse_lazy("dishes:dish-list")

class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "recipe_manager/dish_confirm_delete.html"
    success_url = reverse_lazy("dishes:dish-list")
