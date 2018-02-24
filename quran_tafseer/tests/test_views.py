from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy


class TestTafseerViews(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Bakarah', index=2)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        self.ayah_2 = mommy.make('quran_text.ayah', number=2, sura=self.sura,
                                 text='الحمد لله رب العالمين')
        self.tafseer = mommy.make('quran_tafseer.Tafseer', name='simple',
                                  language='ar', book_name='simple book',
                                  author='random')
        self.tafseer_text = mommy.make('quran_tafseer.TafseerText',
                                       ayah=self.ayah, tafseer=self.tafseer,
                                       text='بسم الله الرحمن الرحيم')

    def test_tafseer_view(self):
        tafseer_url = reverse('tafseer-list')
        response = self.client.get(tafseer_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '[{"id":1,"name":"simple","language":"ar",'
                         '"author":"random","book_name":"simple book"}]')

    def test_tafseer_text_view(self):
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id': 1,
                                                           'sura_index': 2,
                                                           'ayah_number': 1})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/1","ayah_number":1,'
                         '"text":"بسم الله الرحمن الرحيم"}')
        self.assertEqual(response['X-Next-Ayah'], "2:2")

    def test_not_found_tafseer_404(self):
        """
        Test if API gets invalid tafseer id or (Ayah & Sura ids)
        should return 404 NOT FUND status
        """
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id': 0,
                                                           'sura_index': 0,
                                                           'ayah_number': 0})
        response = self.client.get(tafseer_text_url)

        self.assertEqual(404, response.status_code)
        self.assertEqual(
            '{"detail":"Tafseer with provided id or with sura and '
            'ayah ids not found"}',
            response.content.decode())
        with self.assertRaises(KeyError):
            response['X-Next-Ayah']

    def test_get_tafseer_range(self):
        """
        Test getting the tafseer in the same sura but with a range of verses
        """
        # Add more ayah and its tafseer
        mommy.make('quran_tafseer.TafseerText',
                   ayah=self.ayah_2, tafseer=self.tafseer,
                   text='ألم')
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id': 1,
                                                           'sura_index': 2,
                                                           'ayah_from': 1,
                                                           'ayah_to': 2})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '[{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/1'
                         '","ayah_number":1,'
                         '"text":"بسم الله الرحمن '
                         'الرحيم"},'
                         '{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/2","ayah_number":2,'
                         '"text":"ألم"}]')

    def test_get_tafseer_range_with_wrong_numbers(self):
        """
        Test getting the tafseer in the same sura but with a range of verses
        """
        # Add more ayah and its tafseer
        mommy.make('quran_tafseer.TafseerText',
                   ayah=self.ayah_2, tafseer=self.tafseer,
                   text='ألم')
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id': 1,
                                                           'sura_index': 2,
                                                           'ayah_from': 2,
                                                           'ayah_to': 1})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 404)
