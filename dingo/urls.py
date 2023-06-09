"""
URL configuration for dingo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from dingo.api import router

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('maths/', include("maths.urls")),
    path('', include("greetings.urls")),
    path('sessions/', include("sessions.urls")),
    path('posts/', include("posts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('books/', include('books.urls')),
    path('api/v1/', include(router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
