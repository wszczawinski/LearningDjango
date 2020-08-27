from django.urls import path
from . import views

# setting namespace (template url)
app_name = "django_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("user_login/", views.user_login, name="user_login"),
]
