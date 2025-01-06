from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CookUser
from recipe_manager.models import Dish, DishType


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
        self.assertTemplateUsed(response, "recipe_manager/dish_type_list.html")

    def test_dish_type_search(self):
        DishType.objects.create(name="Інша категорія")
        response = self.client.get(
            reverse("recipe_manager:dish-type-list"), {"name": "Тестова"}
        )
        self.assertEqual(len(response.context["dish_types"]), 1)

    def test_dish_type_create_view(self):
        # Неавторизований користувач не може створювати
        response = self.client.post(
            reverse("recipe_manager:dish-type-create"), {"name": "Нова категорія"}
        )
        self.assertEqual(response.status_code, 302)  # Редірект на логін

        # Авторизований користувач може створювати
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("recipe_manager:dish-type-create"), {"name": "Нова категорія"}
        )
        self.assertTrue(DishType.objects.filter(name="Нова категорія").exists())


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
