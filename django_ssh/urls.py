from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('home/', include('django_ssh_public.urls')),
    path('', include('django_ssh_public.urls'))
]