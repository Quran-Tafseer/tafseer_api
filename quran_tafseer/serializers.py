from django.urls import reverse

from rest_framework import serializers

from .models import Tafseer, TafseerText


class TafseerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tafseer
        fields = ['id', 'name']


class TafseerTextSerializer(serializers.ModelSerializer):
    tafseer_id = serializers.IntegerField(source='tafseer.id')
    tafseer_name = serializers.CharField(source='tafseer.name')
    ayah_url = serializers.SerializerMethodField()
    ayah_number = serializers.IntegerField(source='ayah.pk')

    def get_ayah_url(self, obj):
        return reverse('ayah-detail', kwargs={'number': obj.ayah.number,
                                              'sura_num': obj.ayah.sura.pk})

    class Meta:
        model = TafseerText
        fields = ['tafseer_id', 'tafseer_name', 'ayah_url',
                  'ayah_number', 'text']
