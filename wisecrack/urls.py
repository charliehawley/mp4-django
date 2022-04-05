from . import views
from django.urls import path

urlpatterns = [
    path('', views.PromptList.as_view(), name='home')
]