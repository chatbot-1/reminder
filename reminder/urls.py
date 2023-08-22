"""reminder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from reminders.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', log_in, name='login'),
    path('signup/', sign_up, name='signup'),
    path('logout/', log_out, name='logout'),
    path('set-reminder/', setReminder, name='setRem'),
    path('update-reminder/', updateReminder, name='updateRem'),
    path('delete-reminder/', deleteReminder, name='deleteRem'),
    path('delete_reminder/<id>/', delete_reminder, name='delReminder'),
    path('update_reminder/<id>/', update_reminder, name='updReminder'),
    path('view_data/', viewData, name='viewData'),
    path('view_reminder/<id>/', viewRem, name='viewRem'),
]
