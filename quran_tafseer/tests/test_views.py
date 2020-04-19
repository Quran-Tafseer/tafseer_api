import json
import os
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

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
        self.tafseer_text_2 = mommy.make('quran_tafseer.TafseerText',
                                         ayah=self.ayah_2,
                                         tafseer=self.tafseer,
                                         text='الحمد لله رب العالمين')

    def test_tafseer_view(self):
        tafseer_url = reverse('tafseer-list')
        response = self.client.get(tafseer_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '[{"id":1,"name":"simple","language":"ar",'
                         '"author":"random","book_name":"simple book"}]')

    def test_tafseer_list_by_language(self):
        mommy.make('quran_tafseer.Tafseer', name='simple',
                   language='en', book_name='simple book',
                   author='random')
        tafseer_url = os.path.join(reverse('tafseer-list'), '?lang=ar')
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
                         '"ayah_url":"/quran/2/1/","ayah_number":1,'
                         '"text":"بسم الله الرحمن الرحيم"}')
        self.assertEqual(response['X-Next-Ayah'], "2:2")

    def test_tafseer_text_with_no_next_ayah_view(self):
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id': 1,
                                                           'sura_index': 2,
                                                           'ayah_number': 2})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/2/","ayah_number":2,'
                         '"text":"الحمد لله رب العالمين"}')
        self.assertNotIn('x-next-ayah', response)

    def test_not_found_tafseer_404(self):
        """
        Test if API gets invalid tafseer id or (Ayah & Sura ids)
        should return 404 NOT FOUND status
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
            self.assertIsNotNone(response['X-Next-Ayah'])

    def test_get_tafseer_range(self):
        """
        Test getting the tafseer in the same sura but with a range of verses
        """
        tafseer_text_url = reverse('ayah-tafseer-range',
                                   kwargs={'tafseer_id': 1,
                                           'sura_index': 2,
                                           'ayah_from': 1,
                                           'ayah_to': 2})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(),
                         '[{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/1/'
                         '","ayah_number":1,'
                         '"text":"بسم الله الرحمن '
                         'الرحيم"},'
                         '{"tafseer_id":1,"tafseer_name":"simple",'
                         '"ayah_url":"/quran/2/2/","ayah_number":2,'
                         '"text":"الحمد لله رب العالمين"}]')

    def test_get_tafseer_range_with_wrong_numbers(self):
        """
        Test getting the tafseer in the same sura but with a range of verses
        """
        # Add more ayah and its tafseer
        mommy.make('quran_tafseer.TafseerText',
                   ayah=self.ayah_2, tafseer=self.tafseer,
                   text='ألم')
        tafseer_text_url = reverse('ayah-tafseer-range',
                                   kwargs={'tafseer_id': 1,
                                           'sura_index': 2,
                                           'ayah_from': 2,
                                           'ayah_to': 1})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 404)

    def test_tafseer_book_details(self):
        """
        Test getting the Quran Tafseer book details
        """
        tafseer_book_url = reverse('tafseer-book-details',
                                   kwargs={'tafseer_id': 1})
        response = self.client.get(tafseer_book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.content.decode())
        self.assertDictEqual(json.loads(response.content.decode()),
                             {'id': 1,
                              'name': 'simple',
                              'language': 'ar',
                              'book_name': 'simple book',
                              'author': 'random'})

    def test_tafseer_book_details_not_found(self):
        """
        Test getting the Quran Tafseer book details with invalid ID. The API
        should return 404.
        """
        tafseer_book_url = reverse('tafseer-book-details',
                                   kwargs={'tafseer_id': 9999})
        response = self.client.get(tafseer_book_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
