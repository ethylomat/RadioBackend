from django.conf.urls import url, include
from rest_framework import routers

from . import views

app_name = 'channels'


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'channels', views.ChannelsViewSet)


urlpatterns = [url(r'^', include(router.urls)), url(
    r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
