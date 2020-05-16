from django.db import models


class Channel(models.Model):
    title = models.CharField(max_length=140, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    frequency = models.FloatField(blank=True, null=True, default=0)
    media_file = models.FileField(blank=True, null=True)

    def __str__(self):
        return "[%s, %2.2f]" % (self.title, self.frequency)
