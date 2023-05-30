from django.http import HttpResponse
from django.urls import path
from django.views.generic import TemplateView

from .views import welcome_view, about_view, contact_view


app_name='greetings'
urlpatterns = [
    path('', welcome_view, name='welcome'),
    # path('about', about_view, name='about'),
    path('about', TemplateView.as_view(template_name='greetings/about.html'), name='about'),
    # path('contact', contact_view, name='contact'),
    path('contact', TemplateView.as_view(template_name='greetings/contact.html'), name='contact'),
]