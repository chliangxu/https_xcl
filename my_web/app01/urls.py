from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path("computer_info/", views.select_computer_info())
]