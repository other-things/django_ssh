from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('server_information', views.server_information, name='index'),
]