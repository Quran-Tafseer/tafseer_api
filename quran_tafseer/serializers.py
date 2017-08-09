from rest_framework import serializers

from .models import Tafseer, TafseerText


class TafseerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tafseer
        fields = ['id', 'name']


class TafseerTextSerializer(serializers.ModelSerializer):
    tafseer_id = serializers.IntegerField(source='tafseer.id')
    tafseer_name = serializers.CharField(source='tafseer.name')

    class Meta:
        model = TafseerText
        fields = ['tafseer_id', 'tafseer_name', 'ayah', 'text']
