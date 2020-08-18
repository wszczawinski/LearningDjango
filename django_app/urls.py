from django.urls import path
from django_app import views

# setting namespace
app_name = "django_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("users/", views.users, name="users"),
]
