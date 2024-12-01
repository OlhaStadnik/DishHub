from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CookUser

@admin.register(CookUser)
class CookUserAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    search_fields = UserAdmin.search_fields
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("years_of_experience",)}),
    )
