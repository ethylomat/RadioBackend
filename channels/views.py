from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .models import Channel, ChannelSet
from .serializers import ChannelSerializer, ChannelSetSerializer

# API Viewset - Channel (Rest-Framework)
#

class ChannelsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


# API Viewset - ChannelSet (Rest-Framework)
#

class ChannelSetsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChannelSet.objects.all()
    serializer_class = ChannelSetSerializer


# CRUD Operations
# Channel list view

def list(request):
    channels = Channel.objects.order_by('from_frequency')
    context = {"channels": channels}
    return render(request, "list.html", context=context)


# CRUD Operations
# Channel create view

def create(request):
    return render(request, "create.html")


# CRUD Operations
# Channel create view

def edit(request):
    return render(request, "edit.html")