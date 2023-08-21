from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event


# def allEvents(request):
#     event_list = Event.objects.all()
#     for e in event_list:
#         print(e)
#     else:
#         print("There's Nothing Here!")
    
#     return render(request, 'events_list.html',
#                   {'event_list': event_list})