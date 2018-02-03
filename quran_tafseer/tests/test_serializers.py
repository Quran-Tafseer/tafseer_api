from django.test import TestCase
from model_mommy import mommy

from quran_tafseer.serializers import TafseerSerializer, TafseerTextSerializer


class TestTafseerTextSeriazlier(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        self.tafseer = mommy.make('quran_tafseer.Tafseer', name='simple',
                                  language='ar', book_name='simple book',
                                  author='random')
        self.tafseer_text = mommy.make('quran_tafseer.TafseerText',
                                       ayah=self.ayah, tafseer=self.tafseer,
                                       text='بسم الله الرحمن الرحيم')

    def test_tafseer_serializer(self):
        serializer = TafseerSerializer(self.tafseer)
        self.assertEqual(serializer.data, {'id': 1, 'name': 'simple',
                                           'language': 'ar',
                                           'author': 'random',
                                           'book_name': 'simple book'})

    def test_tafseer_text_serializer(self):
        serializer = TafseerTextSerializer(self.tafseer_text)
        self.assertEqual(serializer.data, {'tafseer_id': 1,
                                           'tafseer_name': 'simple',
                                           'ayah_url': '/quran/1/1',
                                           'ayah_number': 1,
                                           'text': 'بسم الله الرحمن الرحيم'})


