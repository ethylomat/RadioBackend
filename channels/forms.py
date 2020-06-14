from django import forms

from .models import Channel, ChannelSet, ChannelFile, ChannelParameter


# Form for creating and editing channels

class ChannelForm(forms.ModelForm):
    class Meta:
         model = Channel
         fields = ('title', 'description', 'from_frequency', 'to_frequency', 'channel_set',)


# Form for deleting channels

class DeleteChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = []
