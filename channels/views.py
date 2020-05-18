from rest_framework import routers, serializers, viewsets
from .models import Channel
from .serializers import ChannelSerializer


# Viewset of Django-REST-Framework for all channels
class ChannelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer