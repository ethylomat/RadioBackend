from django.test import TestCase
from django.apps import apps
from django.conf import settings
from .apps import ChannelsConfig
from .models import Channel


class ChannelTestCase(TestCase):
    def setUp(self):
        Channel.objects.create(title="testtitle", description="testdescription", frequency="0.1")

    def test_channels_to_string(self):
        """The correct string representation is returned"""
        test_channel = Channel.objects.get(title="testtitle")
        self.assertEqual(str(test_channel), '[testtitle, 0.10]')


class ChannelsAppConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ChannelsConfig.name, 'channels')
        self.assertEqual(apps.get_app_config('channels').name, 'channels')
