from __future__ import unicode_literals

from django.test import TestCase

from model_mommy import mommy

from ..serializers import AyahSerializer, SuraSerializer


class QuranTextSerializer(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')

    def test_sura_serailizer(self):
        expected = {
            'index': 1,
            'name': 'Al-Fateha'
        }
        serializer = SuraSerializer(self.sura)
        self.assertDictEqual(expected, serializer.data)

    def test_ayah_serializer(self):
        expected = {
            'sura_index': 1,
            'sura_name': 'Al-Fateha',
            'ayah_number': 1,
            'text': 'بسم الله الرحمن الرحيم'
        }
        serializer = AyahSerializer(self.ayah)
        self.assertDictEqual(expected, serializer.data)
