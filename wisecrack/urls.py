from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PromptList.as_view(), name='home'),
    path('<slug:slug>/', views.PromptDetail.as_view(), name='prompt_detail'),
    path('accounts/', include('allauth.urls')),
]
