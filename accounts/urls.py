from django.urls import path
from .views import (
    CookUserRegisterView,
    # CookUserLoginView,
    # CookUserLogoutView,
    CookUserUpdateView,
    CookUserDetailView,
)

urlpatterns = [
    path("register/", CookUserRegisterView.as_view(), name="register"),
    path("profile/", CookUserDetailView.as_view(), name="profile"),
    path("profile/update/", CookUserUpdateView.as_view(), name="update_profile"),

]

app_name = "accounts"