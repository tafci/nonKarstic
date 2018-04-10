from django.http import JsonResponse
from django.contrib.gis.geos import GEOSGeometry
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
import logging

from common.models import Cave, City, County, Region, Microregion
from common.serializers import CaveListSerializer, CaveDetailedSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
def find_all_cave(request):
    """ Az adatbázisban található barlangokról adok listát szűkített adattartalommal """
    logger.info('Elréhető barlangok listájának lekérése')

    caves = Cave.objects.all()
    serializer = CaveListSerializer(caves)

    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def find_cave_by_id(request, id):
    """ ID alapján az adott barlang adatait adom vissza a hozzá tartozó kiegészítő adatokkal """
    logger.info('Barlang adatainak lekérése > id: {}'.format(id))

    try:
        cave = Cave.objects.get(pk=id)
        serializer = CaveDetailedSerializer(cave)

        return JsonResponse(serializer.data)
    except Cave.DoesNotExist:
        raise NotFound(detail='Megadott azonosítóval nem található bejegyzés az adatbázisban!', code=404)


@api_view(['POST'])
def search_for_cave(request):
    """ Barlagok meghatározott tulajdonságai szerinti leválogatását végzem """
    kozet = request.data['kozet'] if 'kozet' in request.data else None
    vedettseg = request.data['vedettseg'] if 'vedettseg' in request.data else None
    lathatosag = request.data['lathatosag'] if 'lathatosag' in request.data else None
    np = request.data['illetekes_np'] if 'illetekes_np' in request.data else None
    city_id = request.data['city_id'] if 'city_id' in request.data else None
    county_id = request.data['county_id'] if 'county_id' in request.data else None
    region_id = request.data['region_id'] if 'region_id' in request.data else None
    microregion_id = request.data['microregion_id'] if 'microregion_id' in request.data else None

    logger.info("Barlangok leválogatása paraméterek alapján")

    filter_params = {}
    if kozet:
        filter_params['kozet'] = kozet

    if vedettseg:
        filter_params['vedettseg'] = vedettseg

    if lathatosag:
        filter_params['lathatosag'] = lathatosag

    if np:
        filter_params['illetekes_np'] = np

    if city_id:
        try:
            city = City.objects.get(pk=city_id)
            filter_params['geom__coveredby'] = city.geom
        except City.DoesNotExist:
            raise NotFound(detail='Hoppá! A megadott azonosítóval nem létezik város az adatbázisban!', code=404)

    if county_id:
        try:
            county = County.objects.get(pk=county_id)
            filter_params['geom__coveredby'] = county.geom
        except County.DoesNotExist:
            raise NotFound(detail='Hoppá! A megadott azonosítóval nem létezik megye az adatbázisban!', code=404)

    if region_id:
        try:
            microregions = Microregion.objects.filter(nagytaj_id__exact=region_id)
            geos_mregions = GEOSGeometry(microregions[0].geom.wkt)
            microregions = microregions[1:]

            for microregion in microregions:
                geom = GEOSGeometry(microregion.geom.wkt)
                geos_mregions = geos_mregions.union(geom)

            filter_params['geom__coveredby'] = geos_mregions
        except Region.DoesNotExist:
            raise NotFound(detail='Hoppá! A megadott azonosítóval nem létezik nagytáj az adatbázisban!', code=404)

    if microregion_id:
        try:
            microregion = Microregion.objects.get(pk=microregion_id)
            filter_params['geom__coveredby'] = microregion.geom
        except Microregion.DoesNotExist:
            raise NotFound(detail='Hoppá! A megadott azonosítóval nem létezik kistáj az adatbázisban!', code=404)

    try:
        caves = Cave.objects.filter(**filter_params)
        serializer = CaveListSerializer(caves)

        return JsonResponse(serializer.data, safe=False)
    except Cave.DoesNotExist:
        raise NotFound(detail='Hoppá! A megadott paraméterek alapján nem található barlang az adatbázisban!', code=404)
