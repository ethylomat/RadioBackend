from django.urls import path

from . import views


urlpatterns = [
    path(r'channel/edit/<int:pk>/', views.channel_edit, name='channel_edit'),
    path(r'channel/delete/<int:pk>/', views.channel_delete, name='channel_delete'),
    path(r'channel/<int:pk>/', views.channel_detail, name='channel_detail'),
    path(r'channel/create', views.channel_create, name='channel_create'),
    path(r'', views.channel_list, name='channel_list'),
]