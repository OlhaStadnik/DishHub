from django.test import TestCase
from decimal import Decimal

from accounts.models import CookUser
from recipe_manager.models import Dish, DishType


class DishModelTests(TestCase):
    def setUp(self):
        self.cook = CookUser.objects.create_user(
            username="testcook", email="test@example.com", password="testpass123"
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