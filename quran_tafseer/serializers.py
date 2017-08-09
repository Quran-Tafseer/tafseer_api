from rest_framework import serializers

from .models import Tafseer


class TafseerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tafseer
        fields = ['id', 'name']
