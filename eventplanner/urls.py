"""
URL configuration for eventplanner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from event.views import *
from django.conf import settings
from django.conf.urls.static import static
from event.views import logout  

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("login/", signin, name="login"),
    path("signup/", signup, name="signup"),
    path("user_home/", user_home, name="user_home"),
    path("admin_home/", admin_home, name="admin_home"),
    path('view_users/', view_users, name='view_users'), 
    path('upcoming_event/',upcoming_events,name='upcoming_events'),
    path('add_upcoming_event/', add_upcoming_event, name='add_upcoming_event'),
    path('manage_upcoming_event/', manage_upcoming_event, name='manage_upcoming_event'),
    path('update_upcoming_event/<int:event_id>/', update_upcoming_event, name='update_upcoming_event'),
    path('delete_upcoming_event/<int:event_id>/', delete_upcoming_event, name='delete_upcoming_event'),
    path('logout/', logout, name='logout'),
    path('register_event/<int:event_id>/', register_event, name='register_event'),
    path('user_upcoming_event/', user_upcoming_event, name='user_upcoming_event'),  
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    



