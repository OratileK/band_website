from django.urls import path
from django.views.generic import ListView
from . import views
from .models import Event


app_name="events"
urlpatterns = [
    path('', ListView.as_view(queryset = Event.objects.all(), template_name= "events_list.html"), name = "list_events"),
]