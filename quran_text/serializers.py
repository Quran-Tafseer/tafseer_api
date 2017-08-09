from rest_framework import serializers

from .models import Sura, Ayah


class SuraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sura
        fields = ['index', 'name']


class AyahSerializer(serializers.ModelSerializer):
    sura_id = serializers.IntegerField(source='sura.pk')
    sura_name = serializers.CharField(source='sura.name')
    ayah_number = serializers.IntegerField(source='number')

    class Meta:
        model = Ayah
        fields = ['sura_id', 'sura_name', 'ayah_number', 'text']
