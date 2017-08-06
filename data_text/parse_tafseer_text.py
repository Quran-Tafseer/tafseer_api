from quran_text.models import Ayah
from quran_tafseer.models import TafseerText, Tafseer


def parse_tafseer_file(file_name, tafseer_name):
    with open(file_name, 'r') as tafseer_file:
        tafseer = Tafseer.objects.create(name=tafseer_name)
        for line in tafseer_file:
            sura, ayah, text = line.strip().split('|')
            ayah_obj = Ayah.objects.get(number=ayah, sura_id=sura)
            TafseerText.objects.create(ayah=ayah_obj,
                                       text=text,
                                       tafseer=tafseer)
        print('Done parsing file {} and create {} tafseer'.format(file_name,
                                                                  tafseer_name)
              )


def parse_tafseer_muyassar():
    parse_tafseer_file('data_text/ar.muyassar.txt', 'التفسير الميسر')


def parse_tafseer_jalalayn():
    parse_tafseer_file('data_text/ar.jalalayn.txt', 'تفسير الجلالين')
