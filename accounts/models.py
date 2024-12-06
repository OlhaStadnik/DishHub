from django.db import models
from django.contrib.auth.models import AbstractUser


class CookUser(AbstractUser):
    years_of_experience = models.IntegerField(default=0, blank=True, null=True)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=70, unique=True)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
