from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'edit', views.edit),
    url(r'create', views.create),
    url(r'', views.list),
]