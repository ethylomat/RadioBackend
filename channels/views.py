from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import routers, serializers, viewsets
from .models import Channel, ChannelSet
from .forms import ChannelForm, DeleteChannelForm
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

def channel_list(request):
    channels = Channel.objects.order_by('from_frequency')
    context = {"channels": channels}
    return render(request, "channel_list.html", context=context)


# CRUD Operations
# Channel create view

def channel_create(request):
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save(commit=False)
            #channel.description = "Test"
            channel.save()
            return redirect('channel_detail', pk=channel.pk)
    else:
        form = ChannelForm()
    return render(request, 'channel_edit.html', {'form': form})


# CRUD Operations
# Channel create view

def channel_edit(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    if request.method == "POST":
        form = ChannelForm(request.POST, instance=channel)
        if form.is_valid():
            channel = form.save(commit=False)
            #channel.description = "Test"
            channel.save()
            return redirect('channel_detail', pk=channel.pk)
    else:
        form = ChannelForm(instance=channel)
    return render(request, 'channel_edit.html', {'form': form})


# CRUD Operations
# Channel detail view

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    return render(request, 'channel_detail.html', {'channel': channel})


# CRUD Operations
# Channel delete view

def channel_delete(request, pk):
    channel = get_object_or_404(Channel, pk=pk)

    if request.method == 'POST':
        form = DeleteChannelForm(request.POST, instance=channel)
        if form.is_valid(): # checks CSRF
            channel.delete()
            return redirect('channel_list')

    else:
        form = DeleteChannelForm(instance=channel)
    return render(request, 'channel_delete.html', {'form': form, 'channel': channel})