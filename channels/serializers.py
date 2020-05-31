from .models import Channel, ChannelSet, ChannelParameter
from rest_framework import serializers


#  Serializer for Channel (Rest-Framework)
#

class ChannelParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChannelParameter
        fields = ['parameter', 'value']


#  Serializer for Channel (Rest-Framework)
#

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    parameters = ChannelParameterSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'frequency', 'media_file', 'parameters']


# Serializer for ChannelSet (Rest-Framework)
#

class ChannelSetSerializer(serializers.HyperlinkedModelSerializer):
    channels = ChannelSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'title', 'channels']