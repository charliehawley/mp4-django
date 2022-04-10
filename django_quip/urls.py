"""
django_quip URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wisecrack.urls'), name='wisecrack_urls')
]
