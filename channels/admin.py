from django.contrib import admin
from .models import Channel, ChannelSet, ChannelParameter, ChannelFile

admin.site.register(Channel)
admin.site.register(ChannelSet)
admin.site.register(ChannelParameter)
admin.site.register(ChannelFile)