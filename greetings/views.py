from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def greet_world(request):
    return HttpResponse("Hello World!")


def greet_someone(request, name):
    return HttpResponse(f"Hello {name.capitalize()}")