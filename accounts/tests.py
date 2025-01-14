from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from django.db import IntegrityError
from accounts.forms import RegisterForm
from accounts.admin import CookUserAdmin
from accounts.models import CookUser


class CookUserAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()
        self.admin = CookUserAdmin(CookUser, self.site)

    def test_search_fields(self):
        expected_fields = ["username", "first_name", "last_name"]
        for field in expected_fields:
            self.assertIn(field, self.admin.search_fields)

    def test_fieldsets(self):
        found = False
        for fieldset in self.admin.fieldsets:
            if "years_of_experience" in fieldset[1]["fields"]:
                found = True
                break
        self.assertTrue(
            found, "Поле 'years_of_experience' " "не знайдено у fieldsets"
        )

    def test_add_fieldsets(self):
        found = False
        expected_fields = {"first_name", "last_name", "years_of_experience"}
        for fieldset in self.admin.add_fieldsets:
            if set(fieldset[1]["fields"]) & expected_fields:
                found = True
                break
        self.assertTrue(found, "Не знайдено необхідні поля " "у add_fieldsets")


class CookUserTests(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            "username": "testcook",
            "email": "test@example.com",
            "password": "testpass123",
            "first_name": "Test",
            "last_name": "Cook",
            "years_of_experience": 5,
        }
        self.user = CookUser.objects.create_user(**self.user_data)

    def test_create_cook_user(self):
        self.assertEqual(self.user.username, "testcook")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.years_of_experience, 5)

    def test_cook_str_method(self):
        self.assertEqual(str(self.user), "Test Cook")

    def test_unique_email(self):
        with self.assertRaises(IntegrityError):
            CookUser.objects.create_user(
                username="anothercook",
                email="test@example.com",
                password="testpass123",
            )


class RegisterFormTests(TestCase):
    def test_register_form_valid_data(self):
        form_data = {
            "username": "testuser",
            "email": "test@test.com",
            "years_of_experience": 5,
            "password1": "testpass123",
            "password2": "testpass123",
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_passwords_dont_match(self):
        form_data = {
            "username": "testuser",
            "email": "test@test.com",
            "years_of_experience": 5,
            "password1": "testpass123",
            "password2": "testpass456",
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_register_form_invalid_email(self):
        form_data = {
            "username": "testuser",
            "email": "invalid-email",
            "years_of_experience": 5,
            "password1": "testpass123",
            "password2": "testpass123",
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)
