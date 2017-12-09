from django.test import TestCase
from model_mommy import mommy

from quran_tafseer.models import Tafseer, TafseerText


class TestTafseerModel(TestCase):
    def setUp(self):
        self.tafseer = mommy.make(Tafseer, name='simple')

    def test_str(self):
        self.assertEqual(str(self.tafseer), 'simple')


class TestTafseerTextModel(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        self.tafseer = mommy.make(Tafseer, name='simple')
        self.tafseer_text = mommy.make(TafseerText, ayah=self.ayah,
                                       text='بسم الله الرحمن الرحيم')

    def test_str(self):
        self.assertEqual(str(self.tafseer_text), 'بسم الله الرحمن الرحيم')


class TestTafseerTextManager(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah_1 = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                                 text='بسم الله الرحمن الرحيم')
        self.ayah_2 = mommy.make('quran_text.ayah', number=2, sura=self.sura,
                                 text='الحمدلله رب العالمين')
        self.tafseer = mommy.make(Tafseer, name='simple')
        self.tafseer_text_1 = mommy.make(TafseerText, ayah=self.ayah_1,
                                         tafseer=self.tafseer,
                                         text='بسم الله الرحمن الرحيم')
        self.tafseer_text_2 = mommy.make(TafseerText, ayah=self.ayah_1,
                                         tafseer=self.tafseer,
                                         text='الحمدلله رب العالمين')

    def test_get_sura_tafseer(self):
        sura_tafseer = TafseerText.objects.get_sura_tafseer(self.tafseer.pk,
                                                            self.sura.pk)
        self.assertEqual(2, sura_tafseer.count())
        self.assertIn(self.tafseer_text_1, sura_tafseer)
        self.assertIn(self.tafseer_text_2, sura_tafseer)

    def test_ayah_tafseer(self):
        ayah_tafseer = TafseerText.objects.get_ayah_tafseer(self.tafseer.pk,
                                                            self.sura.pk,
                                                            self.ayah_1.pk)
        self.assertEqual(self.tafseer_text_1, ayah_tafseer)

    def test_get_ayah_tafseer_range(self):
        ayah_tafseer_range = TafseerText.objects.get_ayah_tafseer_range(self.tafseer.pk,
                                                                        self.sura.pk,
                                                                        1, 2)
        self.assertEqual(2, ayah_tafseer_range.count())
        self.assertIn(self.tafseer_text_1, ayah_tafseer_range)
        self.assertIn(self.tafseer_text_2, ayah_tafseer_range)
