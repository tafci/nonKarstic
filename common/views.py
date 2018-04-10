from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
import logging

from .models import City, County, Region, Microregion, SOUNDING_ROCK, PROTECTION, ATTENDABILITY, NP
from .serializers import CitySerializer, CountySerializer, RegionSerializer, MicroregionSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
def find_all_city(request):
    """ Az adatbázisban található összes várost, minden adatával együtt listázom """
    logger.info('Városok listájának lekérdezése')

    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)

    if cities.count() > 0:
        return JsonResponse(serializer.data, safe=False)
    else:
        raise NotFound(detail='Hoppá! A városokról nincsenek adataim az adatbázisban!', code=404)


@api_view(['GET'])
def find_all_county(request):
    """ Az adatbázisban található összes megyét, minden adatával együtt listázom """
    logger.info('Megyék listájának lekérdezése')

    counties = County.objects.all()
    serializer = CountySerializer(counties, many=True)

    if counties.count() > 0:
        return JsonResponse(serializer.data, safe=False)
    else:
        raise NotFound(detail='Hoppá! A megyékről nincsenek adataim az adatbázisban!', code=404)


@api_view(['GET'])
def find_county_cities(request, id):
    """ Az adatbázisban található, a megyadott megyéhez tartozó városokat, minden adatával együtt listázom """
    logger.info('Megyéhez tartozó városok listázása')

    try:
        county = County.objects.get(pk=id)
        cities = City.objects.filter(geom__coveredby=county.geom)
        serializer = CitySerializer(cities, many=True)

        return JsonResponse(serializer.data, safe=False)
    except County.DoesNotExist:
        raise NotFound(detail='Hoppá! Ilyen azonosítójú megyét nem találtam az adatbázisban!', code=404)

@api_view(['GET'])
def find_all_region(request):
    """ Az adatbázisban található összes nagytájat, minden adatával együtt listázom """
    logger.info('Nagytájak listájának lekérdezése')

    regions = Region.objects.all()
    serializer = RegionSerializer(regions, many=True)

    if regions.count() > 0:
        return JsonResponse(serializer.data, safe=False)
    else:
        raise NotFound(detail='Hoppá! A nagytájakról nincsenek adataim az adatbázisban!', code=404)


@api_view(['GET'])
def find_region_microregions(request, id):
    """ Az adatbázisban található, a megadott nagytájhoz tartozó kistájakat, minden adatával együtt listázom """
    logger.info('Nagytájhoz tartozó kistájak listázása')

    try:
        Region.objects.get(pk=id)
    except Region.DoesNotExist:
        raise NotFound(detail='Hoppá! Nem találtam ilyen azonosítójú nagytájat az adatbázisban!', code=404)

    microregions = Microregion.objects.filter(nagytaj_id__exact=id)
    serializer = MicroregionSerializer(microregions, many=True)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def find_all_microregion(request):
    """ Az adatbázisban található összes kistájat, minden adatával együtt listázom """
    logger.info('Kistájak listájának lekérdezése')

    microregion = Microregion.objects.all()
    serializer = MicroregionSerializer(microregion, many=True)

    if microregion.count() > 0:
        return JsonResponse(serializer.data, safe=False)
    else:
        raise NotFound(detail='Hoppá! A nagytájakról nincsenek adataim az adatbázisban!', code=404)


@api_view(['GET'])
def get_sounding_rocks(request):
    """ Befoglaló kőzetek listáját adom vissza """
    return JsonResponse(convert_to_dict(SOUNDING_ROCK))


@api_view(['GET'])
def get_protection_levels(request):
    """ Barlangok lehetséges védelmi besorolásait adom vissza """
    return JsonResponse(convert_to_dict(PROTECTION))


@api_view(['GET'])
def get_attendability_levels(request):
    """ Barlangok lehetséges látogathatósági szint listáját adom vissza """
    return JsonResponse(convert_to_dict(ATTENDABILITY))


@api_view(['GET'])
def get_nationalparks(request):
    """ Nemzetiparkok listájával térek vissza """
    return JsonResponse(convert_to_dict(NP))


def convert_to_dict(tuple):
    """ tuple -> dictionary konvetáló vagyok """

    result = {}
    for item in tuple:
        result[item[0]] = item[1]

    return result
