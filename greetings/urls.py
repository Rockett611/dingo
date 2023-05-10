from django.http import HttpResponse
from django.urls import path
from .views import greet_someone, greet_world


urlpatterns = [
    path('', greet_world),
    path('<name>', greet_someone),
]