from django.test import TestCase, Client
from decimal import Decimal
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.models import CookUser
from recipe_manager.models import Dish, DishType
from recipe_manager.forms import (
    DishCreateForm,
    DishSearchForm,
    DishTypeSearchForm,
)


class DishModelTests(TestCase):
    def setUp(self):
        self.cook = CookUser.objects.create_user(
            username="testcook",
            email="test@example.com",
            password="testpass123",
        )
        self.dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Test Description",
            price=Decimal("99.99"),
            dish_type=self.dish_type,
        )
        self.dish.cooks.add(self.cook)

    def test_create_dish(self):
        self.assertEqual(self.dish.name, "Test Dish")
        self.assertEqual(self.dish.description, "Test Description")
        self.assertEqual(self.dish.price, Decimal("99.99"))
        self.assertEqual(self.dish.dish_type, self.dish_type)

    def test_dish_type_str_method(self):
        self.assertEqual(str(self.dish_type), "Main Course")

    def test_dish_cook_relationship(self):
        self.assertEqual(self.dish.cooks.count(), 1)
        self.assertEqual(self.dish.cooks.first(), self.cook)

    def test_cook_dishes_relationship(self):
        self.assertEqual(self.cook.dishes.count(), 1)
        self.assertEqual(self.cook.dishes.first(), self.dish)


class DishTypeViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CookUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.dish_type = DishType.objects.create(name="Тестова категорія")

    def test_dish_type_list_view(self):
        response = self.client.get(reverse("recipe_manager:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "recipe_manager/" "dish_type_list.html"
        )

    def test_dish_type_search(self):
        DishType.objects.create(name="Інша категорія")
        response = self.client.get(
            reverse("recipe_manager:dish-type-list"), {"name": "Тестова"}
        )
        self.assertEqual(len(response.context["dish_types"]), 1)


class DishViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CookUser.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.dish_type = DishType.objects.create(name="Тестова категорія")
        self.dish = Dish.objects.create(
            name="Тестова страва",
            description="Опис",
            dish_type=self.dish_type,
            price=100.00,
        )

    def test_dish_list_view(self):
        response = self.client.get(reverse("recipe_manager:dish-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "recipe_manager/dish_list.html")

    def test_dish_search(self):
        Dish.objects.create(
            name="Інша страва",
            description="Опис",
            dish_type=self.dish_type,
            price=150.00,
        )
        response = self.client.get(
            reverse("recipe_manager:dish-list"), {"name": "Тестова"}
        )
        self.assertEqual(len(response.context["dishes"]), 1)

    def test_dish_create_view(self):
        self.client.login(username="testuser", password="testpass123")
        new_dish_data = {
            "name": "Нова страва",
            "description": "Новий опис",
            "dish_type": self.dish_type.id,
            "price": 200.00,
            "cooks": [self.user.id],
        }
        response = self.client.post(
            reverse("recipe_manager:dish-create"), new_dish_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Dish.objects.filter(name="Нова страва").exists())


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
        )  # name, description, price є обов'язковими

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
