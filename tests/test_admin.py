from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from accounts.admin import CookUserAdmin
from accounts.models import CookUser


class CookUserAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CookUserAdmin(CookUser, self.site)

    def test_search_fields(self):
        """Перевіряємо наявність полів для пошуку"""
        expected_fields = ["username", "first_name", "last_name"]
        for field in expected_fields:
            self.assertIn(field, self.admin.search_fields)

    def test_fieldsets(self):
        """Перевіряємо, чи містять fieldsets поле years_of_experience"""
        found = False
        for fieldset in self.admin.fieldsets:
            if "years_of_experience" in fieldset[1]["fields"]:
                found = True
                break
        self.assertTrue(found, "Поле 'years_of_experience' не знайдено у fieldsets")

    def test_add_fieldsets(self):
        """Перевіряємо, чи містять add_fieldsets необхідні поля"""
        found = False
        expected_fields = {"first_name", "last_name", "years_of_experience"}
        for fieldset in self.admin.add_fieldsets:
            if set(fieldset[1]["fields"]) & expected_fields:
                found = True
                break
        self.assertTrue(found, "Не знайдено необхідні поля у add_fieldsets")
