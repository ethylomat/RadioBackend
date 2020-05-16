import os
from django.test import TestCase, override_settings
from django.core.handlers.asgi import ASGIHandler
from django.core.handlers.wsgi import WSGIHandler
from .asgi import application as asgi_application
from .wsgi import application as wsgi_application
from django.conf import settings


class AsgiTestCase(TestCase):
    """Testing correctly set environment variable and correct type of the
    ASGIHandler
    """

    def test_environment_variable(self):
        self.assertEqual(
            os.environ["DJANGO_SETTINGS_MODULE"],
            "backend.settings")
        self.assertEqual(type(asgi_application), ASGIHandler)


class WsgiTestCase(TestCase):
    """Testing correctly set environment variable and correct type of the
    WSGIHandler
    """

    def test_environment_variable(self):
        self.assertEqual(
            os.environ["DJANGO_SETTINGS_MODULE"],
            "backend.settings")
        self.assertEqual(type(wsgi_application), WSGIHandler)


class UrlsDebugTestCase(TestCase):
    """Testing if urlpatterns for debug are created"""
    settings.DEBUG = True

    def test_debug(self):
        from .urls import urlpatterns
        patterns = [str(urlpattern.pattern) for urlpattern in urlpatterns]
        self.assertEqual("^admin/static/(?P<path>.*)$" in patterns, True)
        self.assertEqual("^media/(?P<path>.*)$" in patterns, True)
        self.assertEqual("api/v1/" in patterns, True)
        self.assertEqual("admin/" in patterns, True)
