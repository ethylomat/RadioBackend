from django.test import TestCase
from .models import Channel

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
