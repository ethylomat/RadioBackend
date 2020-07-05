import os, time, ffmpeg, hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets
from .models import Channel, ChannelSet, ChannelFile, ChannelParameter
from .forms import ChannelForm, DeleteChannelForm, ChannelSetForm, DeleteChannelSetForm
from .serializers import ChannelSerializer, ChannelSetSerializer
from django_file_md5 import calculate_md5

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Function for adding files to channel
#

def add_file_to_channel(channel, file, md5):
    channel_file = ChannelFile.objects.create(media_file=file, channel=channel, file_hash=md5)

def handle_uploaded_file(channel, f, filename):
    channel.files.all().delete()

    md5 = calculate_md5(f)
    filetype = "." + filename.split(".")[-1]
    filepath = os.path.join(BASE_DIR, "media/") + md5 + filetype
    filename = md5 + filetype

    with open(filepath, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    add_file_to_channel(channel, filename, md5)

    convert_file(channel, filepath, filename)

    return filepath, md5


def convert_file(channel, filepath, filename):
    print("Converting files")
    file_title = ".".join(filename.split(".")[:-1])
    filetype = "." + filepath.split(".")[-1]

    base_filepath = os.path.join(BASE_DIR, "media/")

    output_filepath = base_filepath + file_title + ".mp3"
    if not os.path.exists(output_filepath):
        print("Converting to mp3")
        stream = ffmpeg.input(filepath)
        stream = ffmpeg.output(stream, output_filepath)
        ffmpeg.run(stream)
        md5 = hashlib.md5(open(output_filepath,'rb').read()).hexdigest()
        add_file_to_channel(channel, file_title + ".mp3", md5)

    output_filepath = base_filepath + file_title + ".ogg"
    if not os.path.exists(output_filepath):
        print("Converting to ogg")
        stream = ffmpeg.input(filepath)
        stream = ffmpeg.output(stream, output_filepath)
        ffmpeg.run(stream)
        md5 = hashlib.md5(open(output_filepath, 'rb').read()).hexdigest()
        add_file_to_channel(channel, file_title + ".ogg", md5)

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
    channel_instance = get_object_or_404(Channel, pk=pk)
    if request.method == "POST":
        form = ChannelForm(request.POST, instance=channel_instance)
        if form.is_valid():
            channel_instance = form.save(commit=False)

            request_file = request.FILES['file_field']
            if request_file != None:
                handle_uploaded_file(channel_instance, request_file, str(request_file))

            channel_instance.save()
            return redirect('channel_detail', pk=channel_instance.pk)
    else:
        form = ChannelForm(instance=channel_instance)
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