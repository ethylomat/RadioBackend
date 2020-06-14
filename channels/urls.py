from django.urls import path

from . import views


urlpatterns = [
    path(r'channel/edit/<int:pk>/', views.channel_edit, name='channel_edit'),
    path(r'channel/delete/<int:pk>/', views.channel_delete, name='channel_delete'),
    path(r'channel/<int:pk>/', views.channel_detail, name='channel_detail'),
    path(r'channel/create', views.channel_create, name='channel_create'),

    path(r'channelset/edit/<int:pk>/', views.channelset_edit, name='channelset_edit'),
    path(r'channelset/delete/<int:pk>/', views.channelset_delete, name='channelset_delete'),
    path(r'channelset/<int:pk>/', views.channelset_detail, name='channelset_detail'),
    path(r'channelset/create', views.channelset_create, name='channelset_create'),

    path(r'channelset/', views.channelset_list, name='channelset_list'),
    path(r'channel/', views.channel_list, name='channel_list'),

    path(r'', views.channelset_list, name='channelset_list'),
]