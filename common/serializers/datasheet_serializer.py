from rest_framework import serializers
from ..models import DataSheet


class DatasheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSheet
        fields = (
            'ev',
            'feltaras',
            'geologia',
            'morfologia',
            'hidrologia',
            'klima',
            'radon',
            'vedelem',
            'geofizika',
            'oslenytan',
            'regeszet',
            'biologia',
            'denever',
            'terkep',
            'foto',
            'leiras',
        )
