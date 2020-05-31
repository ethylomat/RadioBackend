from .models import Channel, ChannelSet
from rest_framework import serializers


#  Serializer for Channel (Rest-Framework)
#

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'frequency', 'media_file']


# Serializer for ChannelSet (Rest-Framework)
#

class ChannelSetSerializer(serializers.HyperlinkedModelSerializer):
    channels = ChannelSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'title', 'channels']