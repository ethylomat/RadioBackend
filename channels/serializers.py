from .models import Channel, ChannelSet
from rest_framework import serializers

class ChannelSetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title']

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'frequency', 'media_file']