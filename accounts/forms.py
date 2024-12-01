from django.contrib.auth.forms import UserCreationForm
from .models import CookUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CookUser
        fields = ['username', 'email', 'password1', 'password2']