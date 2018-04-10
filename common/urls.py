from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('cities/', views.find_all_city, name='cities'),
    path('counties/', views.find_all_county, name='counties'),
    path('county/<int:id>/cities', views.find_county_cities, name='county_cities'),
    path('regions/', views.find_all_region, name='regions'),
    path('microregions/', views.find_all_microregion, name='microregions'),
    path('region/<int:id>/microregions', views.find_region_microregions, name='region_microregions'),
    path('sounding_rocks/', views.get_sounding_rocks, name='sounding_rocks'),
    path('nationalparks/', views.get_nationalparks, name='nationalparks'),
    path('attendabilities/', views.get_attendability_levels, name='attendabilities'),
    path('protections/', views.get_protection_levels, name='protection_levels'),
]
