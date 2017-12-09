from django.test import TestCase
from django.apps import apps as django_apps


class TestAppConfig(TestCase):
    def setUp(self):
        self.app_config = django_apps.get_app_config('quran_tafseer')

    def test_app_name(self):
        self.assertEqual('quran_tafseer', self.app_config.name)

    def test_app_verbose_name(self):
        self.assertEqual('Quran Tafseer REST API', self.app_config.verbose_name)
