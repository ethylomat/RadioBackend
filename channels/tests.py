from django.test import TestCase
from django.urls import reverse
from .models import Channel

def create_channel(title=None, description=None, frequency=None):
    return Channel.objects.create(title=title, description=description, frequency=frequency)

# Testing the correct return string
#

class ChannelsReturnStringTest(TestCase):
    def test_correct_return_string(self):
        """
        Testing for correct strings of __str__() method
        """
        c1 = Channel(
            title="Test-Title",
            description="Test-Description",
            frequency=0.01,
        )

        c2 = Channel(
            title="Test-Title",
            description="Test-Description",
        )

        c3 = Channel()

        self.assertEqual(str(c1), "[Test-Title, 0.01]")
        self.assertEqual(str(c2), "[Test-Title]")
        self.assertEqual(str(c3), "[None]")


class ChannelIndexViewTests(TestCase):
    def test_list_no_channels(self):
        """
        If no channel exist -> Message is displayed
        """
        response = self.client.get(reverse('channels-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No channels created")
        self.assertQuerysetEqual(response.context['channels'], [])

    def test_list_created_channel(self):
        """
        Test list with created channel
        """
        c1 = create_channel(title="Test-Title", description="Test-Description", frequency=0.01)
        response = self.client.get(reverse('channels-list'))
        self.assertNotContains(response, "No channels created")
        self.assertContains(response, "Test-Title")
        self.assertNotEqual(response.context['channels'], [])