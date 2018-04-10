from rest_framework import serializers
from ..models import City, County, Region, Microregion


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'nev',)


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ('id', 'nev',)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ('id', 'nev',)


class MicroregionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Microregion
        fields = ('id', 'nev',)
