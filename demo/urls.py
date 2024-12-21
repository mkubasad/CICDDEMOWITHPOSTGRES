
from django.urls import path
from . import views

app_name = 'demo'

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("addDoctor/", views.createDoctor, name="addDoctor"),
]