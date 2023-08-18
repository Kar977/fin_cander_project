from django.contrib.auth import views as auth_views
from django.urls import path

from users.views import RegisterView, ProfileView, profile

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    #path("profile/<str:user_name>/", ProfileView.as_view(), name="profile1"),
    path("profile/", profile, name="profile")
]
