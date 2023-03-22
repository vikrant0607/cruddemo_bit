from django.urls import path

from show import views

urlpatterns = [
    path("", views.registration, name="register"),
    path("login", views.user_login, name="user_login"),
    path("profile", views.user_profile, name="profile"),
    path("delete/<int:id>", views.user_delete, name="delete"),
]
