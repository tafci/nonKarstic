from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializers
from ..models import Cave, CaveExtent
from ..serializers import attachment_serializer, datasheet_serializer, cave_extent_serializer


class CaveShortSerializer(gis_serializers.GeoFeatureModelSerializer):
    """
        Barlangi adatok korlátozott sorosítását végzem, mivel a kezdeti megjelenítéshez a teljes
        adattartalom betöltése felesleges mindegy egyes barlang esetében.
    """

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = Cave
        geo_field = 'geom'
        fields = ('pk', 'nev', 'kataszteri_szam', 'kozet', 'vedettseg', 'lathatosag', 'illetekes_np', 'eov_x', 'eov_y',)


class CaveListSerializer(serializers.ListSerializer):
    child = CaveShortSerializer()

    def update(self, instance, validated_data):
        pass


class CaveDetailedSerializer(serializers.ModelSerializer):
    """
        Barlangi adatok teljes körű sorosítását végzem.
    """
    attachments = attachment_serializer.AttachmentSerializer(source='attachment_set', many=True)
    datasheets = datasheet_serializer.DatasheetSerializer(source='datasheet_set', many=True)
    cave_extent = serializers.SerializerMethodField()

    class Meta:
        model = Cave
        fields = (
            'id',
            'kataszteri_szam',
            'nev',
            'szinonimak',
            'leiras',
            'kozet',
            'vedettseg',
            'lathatosag',
            'illetekes_np',
            'eov_x',
            'eov_y',
            'geom',
            'datasheets',
            'attachments',
            'cave_extent',
        )

    def get_cave_extent(self, obj):
        """
            A barlanghoz utoljára hozzáfűzött kiterjedési adatokat gyűjtöm ki és sorosítom
        """
        latest_cave_extent = CaveExtent.objects.last()
        latest_cave_extent_serializer = cave_extent_serializer.CaveExtentSerializer(latest_cave_extent)

        return latest_cave_extent_serializer.data
