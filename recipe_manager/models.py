from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class DishType(models.Model):
    name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name='dishes')
    cooks = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='dishes')

    def __str__(self):
        return (f"{self.dish_type}: "
                f"{self.name}( {self.price}) {self.description} - {self.cooks.name}") #self.name