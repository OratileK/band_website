from django.urls import path
from . import views
from django.views.generic import ListView
from .models import oneEvent


app_name = 'oneDirection'
urlpatterns = [
    path('', views.oneDirection, name = "oneDirection"),
]

