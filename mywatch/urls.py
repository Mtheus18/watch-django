from django.urls import path
from . import views

urlpatterns = [
    path('', views.relogio, name='relogio'),
]