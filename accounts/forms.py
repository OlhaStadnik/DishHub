from django.contrib.auth.forms import UserCreationForm
from .models import CookUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CookUser
        fields = UserCreationForm.Meta.fields + ('email', 'years_of_experience',)

