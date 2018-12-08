from django.apps import apps as django_apps
from django.test import TestCase


class TestAppConfig(TestCase):
    def setUp(self):
        self.app_config = django_apps.get_app_config('quran_text')

    def test_app_name(self):
        self.assertEqual('quran_text', self.app_config.name)

    def test_app_verbose_name(self):
        self.assertEqual('Quran Text REST API', self.app_config.verbose_name)
