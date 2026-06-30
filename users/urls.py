from django.urls import path
from .views import register, login_view, logout_view, users, edit_user

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("users/", users, name="users"),
    path("edit_user/<int:user_id>/", edit_user, name="edit_user")
]