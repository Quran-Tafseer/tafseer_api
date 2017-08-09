from rest_framework import serializers

from .models import Sura, Ayah


class SuraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sura
        fields = ['index', 'name']


class AyahSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ayah
        fields = ['sura', 'number', 'text']
