from django.test import TestCase

from model_mommy import mommy

from ..models import Ayah, Sura


class TestQuranTextEndpointsURI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.sura = mommy.make(Sura, name='Al-Fateha', index=1)
        cls.ayah = mommy.make(Ayah, number=1, sura=cls.sura,
        text='بسم الله الرحمن الرحيم')

    def test_sura_list_url_with_tail_slash(self):
        url_with_tail_slash = '/quran/'
        self.assertEqual(200, self.client.get(url_with_tail_slash).status_code)

    def test_sura_list_url_without_tail_slash(self):
        url_without_tail_slash = '/quran'
        # Root URL can't accept url without tail
        self.assertEqual(301, self.client.get(url_without_tail_slash).status_code)
 
    def test_sura_details_url_with_tail_slash(self):
        url_with_tail_slash = '/quran/1/1/'
        self.assertEqual(200, self.client.get(url_with_tail_slash).status_code)
    
    def test_sura_details_url_without_tail_slash(self):
        url_without_tail_slash = '/quran/1/1'
        self.assertEqual(200, self.client.get(url_without_tail_slash).status_code)
