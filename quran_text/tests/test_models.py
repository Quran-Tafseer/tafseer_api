from django.test import TestCase

from model_mommy import mommy

from ..models import Ayah, Sura


class TestSuraModel(TestCase):
    def setUp(self):
        self.sura = mommy.make(Sura, name='Al-Fateha', index=1)
        self.ayah = mommy.make(Ayah, number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')

    def test_str(self):
        self.assertEqual('Al-Fateha', str(self.sura))


class TestAyahModel(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        mommy.make('quran_text.ayah', number=2, sura=self.sura,
                   text='الحمدلله رب العالمين')

    def test_str(self):
        self.assertEqual('1 - 1', str(self.ayah))


class TestAyahModelManager(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        mommy.make('quran_text.ayah', number=2, sura=self.sura,
                   text='الحمدلله رب العالمين')

    def test_get_sura_text(self):
        ayaht = Ayah.objects.get_sura_text(1)
        self.assertIn(self.ayah, ayaht)
        self.assertEqual(2, ayaht.count())

    def test_get_sura_ayah(self):
        ayah = Ayah.objects.get_sura_ayah(1, 1)
        self.assertIn(self.ayah, ayah)

    def test_get_sura_ayat_range(self):
        ayaht = Ayah.objects.get_sura_ayat_range(1, 1, 2)
        self.assertIn(self.ayah, ayaht)
        self.assertEqual(2, ayaht.count())
