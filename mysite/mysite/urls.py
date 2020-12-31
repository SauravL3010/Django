from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('polls/safe/', include('polls.urls')), # mysite --> urls.py --> lists the main page urls and the admin page. 
    path('admin/', admin.site.urls)
]
