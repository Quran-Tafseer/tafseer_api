from django.urls import reverse

from model_mommy import mommy
from rest_framework.test import APITestCase

from ..models import Ayah, Sura


class TestQuranTextView(APITestCase):
    def setUp(self):
        self.al_fateha = mommy.make(Sura, name='Al-Fateha', index=1)
        self.al_baqrah = mommy.make(Sura, name='Al-Baqrah', index=2)
        self.al_fateha_ayah = mommy.make(Ayah, number=1, sura=self.al_fateha,
                                         text='بسم الله الرحمن الرحيم')
        self.al_baqrah_ayah = mommy.make(Ayah, number=1, sura=self.al_baqrah,
                                         text='بسم الله الرحمن الرحيم')

    def test_sura_list_view(self):
        sura_list_url = reverse('sura-list')
        response = self.client.get(sura_list_url)
        sura_list = ('[{"index":1,"name":"Al-Fateha"}'
                     ',{"index":2,"name":"Al-Baqrah"}]')
        self.assertEqual(sura_list, response.content.decode())

    def test_ayah_text_view(self):
        ayah_url = reverse('ayah-detail', kwargs={'sura_num': 1, 'number': 1})
        response = self.client.get(ayah_url)
        ayah_text = ('{"sura_index":1,"sura_name":"Al-Fateha","ayah_number":1,'
                     '"text":"بسم الله الرحمن الرحيم"}')
        self.assertEqual(ayah_text, response.content.decode())
