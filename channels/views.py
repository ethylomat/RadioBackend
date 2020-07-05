from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets
from .models import Channel, ChannelSet
from .forms import ChannelForm, DeleteChannelForm, ChannelSetForm, DeleteChannelSetForm
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

@login_required
def channel_list(request):
    channels = Channel.objects.order_by('from_frequency')
    context = {"channels": channels}
    return render(request, "channel_list.html", context=context)


# CRUD Operations
# ChannelSet list view

@login_required
def channelset_list(request):
    channelsets = ChannelSet.objects.all()
    context = {"channelsets": channelsets}
    return render(request, "channelset_list.html", context=context)


# CRUD Operations
# Channel create view

@login_required
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
# Channelset create view

@login_required
def channelset_create(request):
    if request.method == "POST":
        form = ChannelSetForm(request.POST)
        if form.is_valid():
            channelset = form.save(commit=False)
            #channelset.description = "Test"
            channelset.save()
            return redirect('channelset_detail', pk=channelset.pk)
    else:
        form = ChannelSetForm()
    return render(request, 'channelset_edit.html', {'form': form})


# CRUD Operations
# Channel create view

@login_required
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
# Channelset create view

@login_required
def channelset_edit(request, pk):
    channelset = get_object_or_404(ChannelSet, pk=pk)
    if request.method == "POST":
        form = ChannelSetForm(request.POST, instance=channelset)
        if form.is_valid():
            channelset = form.save(commit=False)
            #channelset.description = "Test"
            channelset.save()
            return redirect('channelset_detail', pk=channelset.pk)
    else:
        form = ChannelSetForm(instance=channelset)
    return render(request, 'channelset_edit.html', {'form': form})


# CRUD Operations
# Channel detail view

@login_required
def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    return render(request, 'channel_detail.html', {'channel': channel})


# CRUD Operations
# Channelset detail view

@login_required
def channelset_detail(request, pk):
    channelset = get_object_or_404(ChannelSet, pk=pk)
    return render(request, 'channelset_detail.html', {'channelset': channelset})


# CRUD Operations
# Channel delete view

@login_required
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


# CRUD Operations
# Channelset delete view

@login_required
def channelset_delete(request, pk):
    channelset = get_object_or_404(ChannelSet, pk=pk)

    if request.method == 'POST':
        form = DeleteChannelSetForm(request.POST, instance=channelset)
        if form.is_valid(): # checks CSRF
            channelset.delete()
            return redirect('channelset_list')

    else:
        form = DeleteChannelSetForm(instance=channelset)
    return render(request, 'channelset_delete.html', {'form': form, 'channelset': channelset})