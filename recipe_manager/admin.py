from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import DishType, Dish
from accounts.models import CookUser


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'dish_type']
    list_filter = ['dish_type']
    search_fields = ['name', 'dish_type__name']






