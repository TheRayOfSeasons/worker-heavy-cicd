"""api_service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from django.urls import path

from rest_framework import routers


router = routers.DefaultRouter()

v1_api_url_patterns = [
    path('', include('ice_creams.api.v1.urls')),
    path('', include(router.urls))
]

urlpatterns = [
    path('api/', include((v1_api_url_patterns, 'api_v1'), namespace='api_v1')),
    path('ice-creams/', include('ice_creams.urls')),
    path('admin/', admin.site.urls),
]
