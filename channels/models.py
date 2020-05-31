from django.db import models


class ChannelSet(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)

    def __str__(self):
        return self.title


class Channel(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    frequency = models.FloatField(blank=True, null=True, default=0)
    media_file = models.FileField(blank=True, null=True)

    channel_set = models.ForeignKey("ChannelSet", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.title and self.frequency:
            return "[%s, %2.2f]" % (self.title, self.frequency)
        else:
            return "[%s]" % (self.title)