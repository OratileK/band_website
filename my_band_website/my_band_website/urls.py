"""
URL configuration for my_band_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from oneDirection import views

app_name = "my_band"
urlpatterns = [
    path('', include('oneDirection.urls')),
    path('admin/', admin.site.urls),
    path('events/', include('events.urls', namespace = 'events')),
    path('user_authentication/', include('user_authentication.urls')),
    path('user_authentication/', include('django.contrib.auth.urls')),
    
    
]

