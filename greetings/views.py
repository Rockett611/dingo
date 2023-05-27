from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcome_view(request):
    return render(request, 'greetings/welcome.html', {})


def about_view(request):
    return render(request, 'greetings/about.html', {})


def contact_view(request):
    return render(request, 'greetings/contact.html', {})
