from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'edit', views.edit, name='channels-edit'),
    url(r'create', views.create, name='channels-create'),
    url(r'', views.list, name='channels-list'),
]