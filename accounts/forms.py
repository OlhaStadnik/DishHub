from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CookUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    years_of_experience = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = CookUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "years_of_experience",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    def clean_years_of_experience(self):
        years = self.cleaned_data.get("years_of_experience")
        if years is not None and years < 0:
            raise forms.ValidationError(
                "Years of experience cannot be negative"
            )
        return years
