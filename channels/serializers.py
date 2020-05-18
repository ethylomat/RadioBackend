from .models import Channel
from rest_framework import serializers


class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'frequency', 'media_file']