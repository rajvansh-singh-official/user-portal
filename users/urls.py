from django.urls import path
from .views import (
    register,
    login_view,
    logout_view,
    dashboard,
    users,
    view_user,
    interviews
)

urlpatterns = [
    
    # ===== DASHBOARD =====
    
    path(
        "",
        dashboard,
        name="dashboard",
    ),
    
    # ===== AUTHENTICATION =====
    
    path(
        "register/",
        register,
        name="register"
    ),
    
    path(
        "login/",
        login_view,
        name="login"
    ),
    
    path(
        "logout/",
        logout_view,
        name="logout"
    ),
    
    # ===== USERS =====
    
    path(
        "users/",
        users,
        name="users"
    ),
    
    path(
        "users/<int:user_id>/",
        view_user,
        name="view_user"
    ),
    
    # ===== INTERVIEWS =====
    
    path(
        "interviews/",
        interviews,
        name="interviews"
    )
]