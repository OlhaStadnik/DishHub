from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CookUser

@admin.register(CookUser)
class CookUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("first_name", "last_name", "years_of_experience",)}),
    )
    search_fields = ["username", "first_name", "last_name"]
