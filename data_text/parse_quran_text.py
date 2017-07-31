with open('data_text/quran-simple.txt') as quran_text:
    for ayah in quran_text:
        suran_num, ayah_num, ayah_text = ayah.strip().split('|')
        # TODO create model object and insert it
