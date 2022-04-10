from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PromptList.as_view(), name='home'),
    path('<slug:slug>/', views.PromptDetail.as_view(), name='prompt_detail'),
    path('accounts/', include('allauth.urls')),
    path('upvote/<slug:slug>/<int:pk>/<str:user>', views.SubUpvote.as_view(),
         name='sub_upvote'),
    path('sub-list/<int:pk>/', views.UserSubList.as_view(),
         name='user_sub_list'),
    path('<str:prompt>/<int:pk>', views.EditSub.as_view(), name='edit_sub'),
    path('delete-sub/<int:pk>/<str:sub>', views.DeleteSub.as_view(),
         name='delete_sub')
]
