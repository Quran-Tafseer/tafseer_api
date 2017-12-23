from django.test import TestCase
from django.urls import reverse
from model_mommy import mommy


class TestTafsserViews(TestCase):
    def setUp(self):
        self.sura = mommy.make('quran_text.sura', name='Al-Fateha', index=1)
        self.ayah = mommy.make('quran_text.ayah', number=1, sura=self.sura,
                               text='بسم الله الرحمن الرحيم')
        self.tafseer = mommy.make('quran_tafseer.Tafseer', name='simple')
        self.tafseer_text = mommy.make('quran_tafseer.TafseerText',
                                       ayah=self.ayah, tafseer=self.tafseer,
                                       text='بسم الله الرحمن الرحيم')

    def test_tafseer_view(self):
        tafseer_url = reverse('tafseer-list')
        response = self.client.get(tafseer_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), '[{"id":1,"name":"simple"}]')

    def test_tafseer_text_view(self):
        tafseer_text_url = reverse('ayah-tafseer', kwargs={'tafseer_id':1,
                                                           'sura_index':1,
                                                           'ayah_number':1})
        response = self.client.get(tafseer_text_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), '{"tafseer_id":1,"tafseer_name":"simple",'
                                                    '"ayah_url":"/quran/1/1","ayah_number":1,'
                                                    '"text":"بسم الله الرحمن الرحيم"}')

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
        self.assertEqual('{"detail":"Tafseer with provided id or with sura and ayah ids not found"}',
                         response.content.decode())
