from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Channel
from .serializers import ChannelSerializer

# API Viewset (Rest-Framework)
#

class ChannelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


# Channel list view
#

def list(request):
    channels = Channel.objects.order_by('frequency')
    context = {"channels": channels}
    return render(request, "list.html", context=context)
