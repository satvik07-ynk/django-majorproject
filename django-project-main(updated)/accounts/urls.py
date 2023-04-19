from django.urls import path ,include
from .views import Home
from . import views

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("Equipments/",views.Equipments,name="Equipments"),
    path("Measurements/",views.test, name="test"),
    path("Option_1/",views.Option_1,name="Option_1"),
    path("Option_1/",views.Option_1,name="Option_1"),
    ]