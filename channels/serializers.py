from .models import Channel, ChannelSet, ChannelParameter, ChannelFile
from rest_framework import serializers


#  Serializer for Channel (Rest-Framework)
#

class ChannelParameterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChannelParameter
        fields = ['parameter', 'value']


#  Serializer for File (Rest-Framework)
#

class ChannelFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChannelFile
        fields = ['id', 'media_file', 'extension', 'file_hash']


#  Serializer for Channel (Rest-Framework)
#

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    parameters = ChannelParameterSerializer(many=True)
    files = ChannelFileSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'from_frequency', 'to_frequency', 'files', 'parameters']


# Serializer for ChannelSet (Rest-Framework)
#

class ChannelSetSerializer(serializers.HyperlinkedModelSerializer):
    channels = ChannelSerializer(many=True)

    class Meta:
        model = Channel
        fields = ['id', 'title', 'channels']