from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("counter/", views.counter, name="")
]


urlpatterns = [
    path("", views.index, name="index"),
    path("calculator/", views.calculator, name="")
]