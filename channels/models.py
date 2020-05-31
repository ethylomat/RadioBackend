import os
from django.db import models


class ChannelParameter(models.Model):
    parameter = models.CharField(max_length=2048, blank=True, null=True)
    value = models.CharField(max_length=2048, blank=True, null=True)

    channel = models.ForeignKey("Channel", related_name='parameters', on_delete=models.CASCADE, blank=True, null=True)


class ChannelFile(models.Model):
    media_file = models.FileField(blank=True, null=True)

    channel = models.ForeignKey("Channel", related_name='files', on_delete=models.CASCADE, blank=True, null=True)

    def filename(self):
        fileName, fileExtension = os.path.splitext(self.media_file.name)
        return fileName

    def extension(self):
        fileName, fileExtension = os.path.splitext(self.media_file.name)
        return fileExtension


class ChannelSet(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.title


class Channel(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    from_frequency = models.FloatField(blank=True, null=True, default=0)
    to_frequency = models.FloatField(blank=True, null=True, default=0)

    channel_set = models.ForeignKey("ChannelSet", related_name='channels', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.title and self.from_frequency and self.to_frequency:
            return "[%s, %2.2f - %2.2f]" % (self.title, self.from_frequency, self.to_frequency)
        else:
            return "[%s]" % (self.title)