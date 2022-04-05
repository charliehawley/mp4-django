from . import views
from django.urls import path

urlpatterns = [
    path('', views.PromptList.as_view(), name='home'),
    path('<slug:slug>/', views.PromptDetail.as_view(), name='prompt_detail')
]
