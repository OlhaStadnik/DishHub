from django.test import TestCase
from django.contrib.auth import get_user_model
from recipe_manager.forms import DishCreateForm, DishSearchForm, DishTypeSearchForm
from recipe_manager.models import DishType, Dish
from accounts.forms import RegisterForm

class DishCreateFormTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main Course")
        self.user = get_user_model().objects.create_user(
            username="testcook",
            password="testpass123",
            email="test@test.com",
            years_of_experience=3,
        )

    def test_dish_create_form_valid_data(self):
        form_data = {
            "name": "Test Dish",
            "description": "Test Description",
            "price": "10.99",
            "dish_type": self.dish_type.id,
            "cooks": [self.user.id],
        }
        form = DishCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_create_form_no_data(self):
        form = DishCreateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            len(form.errors), 3
        )

    def test_dish_create_form_optional_fields(self):
        form_data = {
            "name": "Test Dish",
            "description": "Test Description",
            "price": "10.99",
        }
        form = DishCreateForm(data=form_data)
        self.assertTrue(form.is_valid())


class SearchFormsTests(TestCase):
    def test_dish_search_form_valid(self):
        form_data = {"name": "Test"}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_search_form_empty(self):
        form_data = {"name": ""}
        form = DishSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form_valid(self):
        form_data = {"name": "Main"}
        form = DishTypeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())