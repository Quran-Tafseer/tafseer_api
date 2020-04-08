from django.test import TestCase

from model_mommy import mommy

from quran_tafseer.models import Tafseer, TafseerText


class TestQuranTafseerEndpointsURI(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        cls.ayah_1 = mommy.make('quran_text.ayah', number=1, sura=cls.sura,
                                text='بسم الله الرحمن الرحيم')
        cls.ayah_2 = mommy.make('quran_text.ayah', number=2, sura=cls.sura,
                                text='الحمدلله رب العالمين')
        cls.tafseer = mommy.make(Tafseer, name='simple')
        cls.tafseer_text_1 = mommy.make(TafseerText, ayah=cls.ayah_1,
                                        tafseer=cls.tafseer,
                                        text='بسم الله الرحمن الرحيم')
        cls.tafseer_text_2 = mommy.make(TafseerText, ayah=cls.ayah_1,
                                        tafseer=cls.tafseer,
                                        text='الحمدلله رب العالمين')

    def test_tafseer_list_with_tail_slash(self):
        url_with_tail_slash = '/tafseer/'
        self.assertEqual(200, self.client.get(url_with_tail_slash).status_code)

    def test_tafseer_list_without_tail_slash(self):
        url_without_tail_slash = '/tafseer'
        # Root URL can't accept url without tail
        self.assertEqual(301, self.client.get(
            url_without_tail_slash).status_code)

    def test_ayah_tafseer_with_tail_slash(self):
        url_with_tail_slash = '/tafseer/1/1/1/'
        self.assertEqual(200, self.client.get(url_with_tail_slash).status_code)

    def test_ayah_tafseer_without_tail_slash(self):
        url_without_tail_slash = '/tafseer/1/1/1'
        self.assertEqual(200, self.client.get(
            url_without_tail_slash).status_code)

    def test_ayah_tafseer_range_with_tail_slash(self):
        url_with_tail_slash = '/tafseer/1/1/1/2/'
        self.assertEqual(200, self.client.get(url_with_tail_slash).status_code)

    def test_ayah_tafseer_range_without_tail_slash(self):
        url_without_tail_slash = '/tafseer/1/1/1/2'
        self.assertEqual(200, self.client.get(
            url_without_tail_slash).status_code)
