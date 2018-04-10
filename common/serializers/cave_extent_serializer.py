from rest_framework import serializers
from ..models import CaveExtent


class CaveExtentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaveExtent
        fields = (
            'hossz',
            'vertikalis',
            'melyseg',
            'magassag',
        )
