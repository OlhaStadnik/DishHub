from django.urls import path
from .views import (
    CookUserRegisterView,
    # CookUserLoginView,
    # CookUserLogoutView,
    CookUserUpdateView,
    CookUserDetailView,
    CookUserListView,
)

urlpatterns = [
    path("register/", CookUserRegisterView.as_view(), name="register"),
    path("cooks/", CookUserListView.as_view(), name="cooks"),
    path("profile/<int:pk>/", CookUserDetailView.as_view(), name="profile"),
    path("profile/update/", CookUserUpdateView.as_view(), name="update_profile"),

]
app_name = "accounts"
