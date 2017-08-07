from rest_framework import serializers

from .models import Sura


class SuraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sura
        fields = ['index', 'name']
