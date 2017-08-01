from quran_text.models import Ayah


with open('data_text/quran-simple.txt') as quran_text:
    for ayah in quran_text:
        sura_num, ayah_num, ayah_text = ayah.strip().split('|')
        Ayah.objects.create(number=ayah_num, sura_id=sura_num, text=ayah_text)
